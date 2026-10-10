#!/usr/bin/env python3
"""Kiểm tra artwork Linh Thú Học Viện theo art_pipeline_spec.md.
Dùng:  python3 tools/check_assets.py [--thumbs] [thư_mục_assets=assets/monsters] [monsters_104.json]
Kiểm tra: tên file, PNG RGBA, 1024x1024, nền trong suốt (4 góc), viền không bị cắt, nhân vật chiếm 75-85% khung, nền không đặc.
--thumbs : tạo thêm bản 256x256 vào <thư mục>/thumbs/ (cùng tên file) cho file đạt chuẩn."""
import sys,json,os
from PIL import Image
args=[a for a in sys.argv[1:] if not a.startswith('--')];thumbs='--thumbs' in sys.argv
folder=args[0] if args else 'assets/monsters';meta=args[1] if len(args)>1 else 'monsters_104.json'
mons=json.load(open(meta,encoding='utf8'))['monsters']
ok=warn=bad=missing=0;report=[]
for m in mons:
    fn=m['asset_filename'];path=os.path.join(folder,fn);code=m['Mã ID']
    if not os.path.exists(path): missing+=1;report.append((code,'THIẾU',fn));continue
    errs=[];warns=[]
    try:
        im=Image.open(path)
        if im.format!='PNG': errs.append('không phải PNG')
        if im.mode!='RGBA': errs.append(f'chế độ {im.mode}, cần RGBA')
        if im.size!=(1024,1024): errs.append(f'kích thước {im.size[0]}x{im.size[1]}, cần 1024x1024')
        if not errs:
            a=im.getchannel('A');W,H=im.size
            if any(a.getpixel(c)>8 for c in [(0,0),(W-1,0),(0,H-1),(W-1,H-1)]): errs.append('nền không trong suốt (góc ảnh có alpha)')
            bb=a.point(lambda v:255 if v>16 else 0).getbbox()
            if not bb: errs.append('ảnh trống')
            else:
                x0,y0,x1,y1=bb;share=max(x1-x0,y1-y0)/W
                if x0<=2 or y0<=2 or x1>=W-2 or y1>=H-2: errs.append('nhân vật/hiệu ứng chạm mép ảnh (bị crop)')
                elif not .70<=share<=.90: warns.append(f'nhân vật chiếm {share:.0%} khung (nên 75–85%)')
            op=sum(a.resize((64,64)).histogram()[241:])/4096
            if op>.97: errs.append('gần như không có vùng trong suốt (nghi ảnh còn nền)')
    except Exception as e: errs.append(f'không đọc được: {e}')
    if errs: bad+=1;report.append((code,'LỖI','; '.join(errs)))
    else:
        if warns: warn+=1;report.append((code,'CẢNH BÁO','; '.join(warns)))
        else: ok+=1
        if thumbs:
            os.makedirs(os.path.join(folder,'thumbs'),exist_ok=True);im.resize((256,256),Image.LANCZOS).save(os.path.join(folder,'thumbs',fn))
for r in report: print(*r,sep=' | ')
print(f'\nĐạt: {ok} · Cảnh báo: {warn} · Lỗi: {bad} · Thiếu: {missing} · Tổng: {len(mons)}')
sys.exit(1 if bad or missing else 0)
