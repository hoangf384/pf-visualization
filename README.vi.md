# Bảng Điều Khiển Tài Chính Cá Nhân (Tableau)

[Read in English](README.md)

## Mục Lục
- [Dự án này là gì?](#dự-án-này-là-gì)
- [T học được gì từ dự án này?](#t-học-được-gì-từ-dự-án-này)
- [Phát hiện thú vị nhất từ dữ liệu](#phát-hiện-thú-vị-nhất-từ-dữ-liệu)
- [Đề xuất cải tiến](#đề-xuất-cải-tiến)
- [Công cụ sử dụng](#công-cụ-sử-dụng)
- [Hướng phát triển tiếp theo](#hướng-phát-triển-tiếp-theo)
- [Cách chạy dự án](#cách-chạy-dự-án)
- [Ảnh chụp màn hình](#ảnh-chụp-màn-hình)

---

## Dự án này là gì?

Dự án phân tích hành vi tài chính cá nhân — bao gồm thu nhập, chi tiêu, và tiết kiệm — theo từng nhóm tuổi.

Vì không có dữ liệu thực từ người dùng, t tự **tạo ra bộ dữ liệu mô phỏng 20.000 dòng** bằng Python, dựa trên số liệu thống kê thực tế từ Bộ Lao động Mỹ ([bls.gov](https://www.bls.gov/cex/tables.htm)). Sau đó trực quan hóa bằng Tableau.

Để hiểu toàn bộ dự án, xem theo thứ tự:

1. **BaoCao_phu_Nhom_10.pdf** — Giải thích cách dữ liệu được tạo ra.
2. **Synthetic_data_generation.ipynb** — Code Python tạo dữ liệu.
3. **BaoCao_Nhom_10.pdf** — Báo cáo phân tích chính.
4. **Income Spending and Saving Overview.twbx** — Dashboard tổng quan toàn dân số.
5. **Actual Spending Behavior Analysis.twbx** — Dashboard phân tích chi tiết từng cá nhân.

```text
pf-visualization/
├── Reports/         ← Báo cáo PDF
├── Notebooks/       ← Code Python
├── Dashboards/      ← File Tableau (.twbx)
└── Data/            ← Dữ liệu CSV
```

---

## T học được gì từ dự án này?

- **Tạo dữ liệu mô phỏng (Synthetic Data):** Học cách dùng Python để tạo dữ liệu giả nhưng có phân phối và logic giống thực tế — rất hữu ích khi không có dữ liệu thật để phân tích.
- **Tableau:** Từ không biết gì đến tự build được 2 dashboard có KPI, bộ lọc tương tác, và biểu đồ xu hướng.
- **Đọc dữ liệu theo nhóm:** Học cách nhìn số theo từng phân khúc (tuổi, nghề nghiệp, khu vực) để tìm ra sự khác biệt có ý nghĩa.
- **Kể chuyện bằng số:** Từ một đống CSV → báo cáo rõ ràng, có kết luận cụ thể.

---

## Phát hiện thú vị nhất từ dữ liệu

Sau khi chạy phân tích (`analyze_pf.py`) trên 20.000 dòng dữ liệu, kết quả theo nhóm tuổi như sau:

| Nhóm tuổi | Tỷ lệ tiết kiệm trung bình | Ý nghĩa |
|-----------|---------------------------|---------|
| 18–25 | **–26.9%** | Đang tiêu nhiều hơn kiếm được |
| 26–35 | +15.6% | Bắt đầu ổn định hơn |
| 36–45 | **+28.7%** | Tiết kiệm tốt nhất |
| 46–55 | +1.9% | Gần như không tiết kiệm — có thể đang nuôi con |
| 56–65 | –86.6% | Đang rút tiền tích lũy (có thể đã về hưu) |

**Điều bất ngờ:** Chi tiêu không thiết yếu (ăn ngoài, giải trí, linh tinh) chỉ chiếm **~8%** tổng chi tiêu — không phải nguyên nhân chính khiến nhóm 18–25 tiêu hết tiền.

> **Kết luận thực sự:** Nhóm trẻ tiêu vượt thu nhập là vì **thu nhập còn thấp trong khi chi phí cố định (thuê nhà, bảo hiểm, đi lại) đã rất cao** — không phải vì họ đi ăn nhiều hay mua sắm nhiều.

---

## Đề xuất cải tiến

Dựa trên kết quả phân tích, nếu muốn giúp người dùng quản lý tiền tốt hơn, t đề xuất thử nghiệm tính năng sau:

### Thử nghiệm A/B: Cảnh báo chi tiêu thông minh

**Vấn đề cần giải quyết:** Nhóm 18–25 đang tiêu nhiều hơn kiếm (–26.9%), nhưng dashboard hiện tại chỉ hiển thị số liệu sau khi đã tiêu xong — quá muộn để thay đổi hành vi.

**Ý tưởng test:**

| | Nhóm A (hiện tại) | Nhóm B (thử nghiệm) |
|---|---|---|
| Trải nghiệm | Xem lại số liệu cuối tháng | Nhận cảnh báo ngay khi chi tiêu sắp vượt thu nhập |
| Ví dụ | "Tháng này bạn đã tiêu 8 triệu" | "⚠️ Bạn đã tiêu 90% thu nhập, còn 10 ngày nữa mới đến tháng sau" |

**Muốn đo lường gì:** Sau 1 tháng, nhóm B có tiết kiệm được nhiều hơn nhóm A không?

**Tại sao cách này đúng hướng:**
Vấn đề không phải thiếu thông tin — người dùng biết họ đang tiêu nhiều. Vấn đề là họ nhận ra **quá muộn**. Cảnh báo sớm (proactive) thay vì báo cáo sau (reactive) mới là can thiệp đúng chỗ.

---

## Công cụ sử dụng

| Công cụ | Dùng để làm gì |
|---------|---------------|
| Python (Pandas, NumPy) | Tạo và làm sạch dữ liệu mô phỏng |
| Tableau | Vẽ dashboard, KPI, biểu đồ |
| Excel / Google Sheets | Kiểm tra và xác thực dữ liệu |

---

## Hướng phát triển tiếp theo

- **Kết nối dữ liệu thật:** Thay dữ liệu mô phỏng bằng export từ app ngân hàng hoặc ví điện tử.
- **Dự báo chi tiêu:** Dùng machine learning để dự đoán tháng này sẽ tiêu bao nhiêu dựa trên lịch sử.
- **Tự động hóa:** Thay vì chạy notebook thủ công, build pipeline tự động cập nhật dashboard mỗi tuần.

---

## Cách chạy dự án

### Clone về máy

```bash
git clone https://github.com/hoangf384/pf-visualization.git
cd pf-visualization
```

### Cài đặt môi trường

```bash
# Tạo môi trường ảo
python -m venv .venv

# Kích hoạt (macOS/Linux)
source .venv/bin/activate
# Kích hoạt (Windows)
.venv\Scripts\activate

# Cài thư viện
pip install -r requirements.txt

# Đăng ký kernel để chạy trong Jupyter
python -m ipykernel install --user --name=.venv --display-name "Python (.venv)"
```

Sau đó mở file `.ipynb` trong Jupyter và chọn kernel **Python (.venv)**.

---

## Ảnh chụp màn hình

![Tổng Quan Nhóm Nhân Khẩu Học](Images/demographic.png)
[→ Xem Dashboard Tổng Quan trên Tableau Public](https://public.tableau.com/app/profile/nguy.n.phan.ho.ng.ph.c/viz/Book1_17516920190310/General?publish=yes)

![Hành Vi Chi Tiêu](Images/Behaviors.png)
[→ Xem Dashboard Hành Vi Chi Tiêu trên Tableau Public](https://public.tableau.com/app/profile/nguyen.nhi8170/viz/CuoiKy_17519870918010/Dashboard1?publish=yes)
