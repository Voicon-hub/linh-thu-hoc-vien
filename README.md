# Linh Thú Học Viện — gói đưa lên GitHub Pages

1. Tạo repository **Public**, ví dụ `linh-thu-hoc-vien`.
2. Upload TOÀN BỘ nội dung thư mục này (giữ nguyên cấu trúc; `index.html` ở thư mục gốc).
3. Settings → Pages → Deploy from a branch → `main` / `(root)` → Save.
4. Mở `https://<tên-bạn>.github.io/linh-thu-hoc-vien/`.
   - Android (Chrome): menu ⋮ → Cài đặt ứng dụng / Thêm vào màn hình chính.
   - iPhone (Safari): Chia sẻ → Thêm vào Màn hình chính.

## Cập nhật sau này
Thay `index.html` (và đổi số phiên bản trong `sw.js`, ví dụ `linh-thu-v23`) rồi commit.

## Danh mục quái vật
`monsters_40.json`: 40 quái vật (8 hệ × 5 độ hiếm), xuất từ file Excel. Game đã nhúng sẵn dữ liệu này trong `index.html`.

## Thẻ quái vật nhiều lớp (assets/ui/)
Ảnh trong `assets/ui/` là các lớp độc lập đã tách nền: `frame_*.png` (khung 8 nguyên tố), `effect_blue/purple/red.png` (vòng ma pháp 4-6 / 7-9 / 10 sao), `star_gold/rainbow.png`, `badge_N/R/SR/SSR/LR.png`. Game đã nhúng sẵn các lớp này.

## Nền màn hình (assets/bg/)
`bg_home.jpg`, `bg_academy.jpg`, `bg_summon.jpg`: nền của Trang chủ, Học viện và Triệu hồi (game đã nhúng sẵn trong `index.html`).

## Hoạt cảnh triệu hồi (assets/summon/)
5 khung của hoạt cảnh (trứng thiêng, vết nứt, bùng sáng, chân thú, bệ đá). Game đã nhúng sẵn trong `index.html`.

## Artwork quái vật
Hiện có ảnh thật cho 25 quái vật: hệ Hỏa (001–005), Thủy (006–010), Lôi (016–020), Phong (021–025), Thổ (026–030). Hệ Mộc, Ánh Sáng, Bóng Tối dùng artwork vector dự phòng.
Các quái vật còn lại chép vào `assets/monsters/` theo tên `mon_001.png … mon_040.png` (PNG RGBA 1024×1024, nền trong suốt, không chữ/khung/sao trong ảnh).
Kiểm tra trước khi tải lên: `python3 tools/check_assets.py --thumbs`. Trong game: Hồ sơ → "Kiểm tra 40 file artwork".

## Lưu ý
Tiến độ lưu trong trình duyệt của từng thiết bị (localStorage), chưa đồng bộ giữa điện thoại và máy tính.
Nút "Công cụ thử nghiệm" ở màn Hồ sơ nên bỏ trước khi chia sẻ link công khai.
