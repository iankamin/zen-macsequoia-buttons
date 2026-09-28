# Cuts each button state out of the Aurorae theme SVGs into tools/build/.
import os, re, copy, xml.etree.ElementTree as ET
SVG='http://www.w3.org/2000/svg'
ET.register_namespace('', SVG)
SRC=os.path.expanduser('~/.local/share/aurorae/themes/MacSequoia-Dark/')
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'build')
os.makedirs(OUT,exist_ok=True)
def parse_tf(s):
    m=[1,0,0,1,0,0]
    for name,args in re.findall(r'(\w+)\s*\(([^)]*)\)', s or ''):
        a=[float(x) for x in re.split(r'[\s,]+',args.strip()) if x]
        if name=='translate': t=[1,0,0,1,a[0],a[1] if len(a)>1 else 0]
        elif name=='scale': t=[a[0],0,0,a[1] if len(a)>1 else a[0],0,0]
        elif name=='matrix': t=a
        else: raise SystemExit('unsupported '+name)
        m=mul(m,t)
    return m
def mul(A,B):
    a,b,c,d,e,f=A; g,h,i,j,k,l=B
    return [a*g+c*h, b*g+d*h, a*i+c*j, b*i+d*j, a*k+c*l+e, b*k+d*l+f]
def find_path(root,target):
    def rec(el,chain):
        if el is target: return chain
        for ch in el:
            r=rec(ch,chain+[ch]); 
            if r: return r
    return rec(root,[root])
def is_glyph(el):
    st=el.get('style','')
    fill=re.search(r'(?<![-a-z])fill:([^;]+)',st)
    op=re.search(r'(?<![-a-z])opacity:([^;]+)',st)
    return bool(fill and fill.group(1)=='#000000' and op and float(op.group(1))==0.5)
states={'active-center':'normal','inactive-center':'inactive','hover-center':'hover','pressed-center':'pressed','hover-inactive-center':'hover-inactive'}
for btn in ['close','minimize','maximize','restore']:
    tree=ET.parse(SRC+btn+'.svg'); root=tree.getroot()
    for g in root.iter('{%s}g'%SVG):
        st=states.get(g.get('id'))
        if not st: continue
        chain=find_path(root,g)
        m=[1,0,0,1,0,0]
        for el in chain[1:]: m=mul(m,parse_tf(el.get('transform')))
        rect=next(r for r in g if r.tag=='{%s}rect'%SVG and r.get('width')=='16')
        x,y=float(rect.get('x')),float(rect.get('y'))
        assert m[1]==0 and m[2]==0 and m[0]==1 and m[3]==1, (btn,st,m)
        X,Y=m[4]+x,m[5]+y
        # outer transform = everything above g; g keeps its own transform
        outer=[1,0,0,1,0,0]
        for el in chain[1:-1]: outer=mul(outer,parse_tf(el.get('transform')))
        out=ET.Element('{%s}svg'%SVG,{'viewBox':f'{X:.4f} {Y:.4f} 16 16','width':'16','height':'16'})
        wrap=ET.SubElement(out,'{%s}g'%SVG,{'transform':'matrix(%s)'%','.join(f'{v:.6g}' for v in outer)})
        gc=copy.deepcopy(g)
        for el in gc.iter():
            for k in list(el.attrib):
                if k.startswith('{') or k in('id',): del el.attrib[k]
        wrap.append(gc)
        s=ET.tostring(out,encoding='unicode')
        s=re.sub(r'\s+',' ',s)
        open(os.path.join(OUT,f'{btn}-{st}.svg'),'w').write(s)
        print(btn,st,len(s))
        if st=='hover':
            # The glyph on its own: drop the coloured circle and the invisible
            # sizing rect, keeping only the 50%-black symbol shapes
            parents={ch:p for p in gc.iter() for ch in p}
            for el in list(gc.iter()):
                if el.tag.split('}')[1] in ('path','rect','circle') and not is_glyph(el):
                    parents[el].remove(el)
            s=re.sub(r'\s+',' ',ET.tostring(out,encoding='unicode'))
            open(os.path.join(OUT,f'{btn}-glyph.svg'),'w').write(s)
            print(btn,'glyph',len(s))
