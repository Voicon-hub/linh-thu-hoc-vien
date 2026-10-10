# Linh Thú Học Viện — gói đưa lên GitHub Pages

1. Tạo repository **Public**, ví dụ `linh-thu-hoc-vien`.
2. Upload TOÀN BỘ nội dung thư mục này (giữ nguyên cấu trúc; `index.html` ở thư mục gốc).
3. Settings → Pages → Deploy from a branch → `main` / `(root)` → Save.
4. Mở `https://<tên-bạn>.github.io/linh-thu-hoc-vien/`.
   - Android (Chrome): menu ⋮ → Cài đặt ứng dụng / Thêm vào màn hình chính.
   - iPhone (Safari): Chia sẻ → Thêm vào Màn hình chính.

## Cập nhật sau này
Thay `index.html` (và đổi số phiên bản trong `sw.js`, ví dụ `linh-thu-v7`) rồi commit.

## Artwork quái vật
Chép 104 file `mon_001.png … mon_104.png` (PNG RGBA 1024×1024, nền trong suốt) vào `assets/monsters/`.
Kiểm tra trước khi tải lên: `python3 tools/check_assets.py --thumbs`.
Game tự dùng ảnh thật khi có; chưa có thì dùng artwork vector dự phòng.

## Lưu ý
Tiến độ lưu trong trình duyệt của từng thiết bị (localStorage), chưa đồng bộ giữa điện thoại và máy tính.
