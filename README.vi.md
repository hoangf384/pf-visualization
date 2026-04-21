# Phân Tích Dữ Liệu Tài Chính Cá Nhân (FinTech / Digital Banking)

[Read in English](README.md)

## Mục Lục
- [Bối cảnh dự án](#bối-cảnh-dự-án)
- [Cách chúng tôi mô phỏng dữ liệu](#cách-chúng-tôi-mô-phỏng-dữ-liệu)
- [Insight quan trọng & Giá trị kinh doanh](#insight-quan-trọng--giá-trị-kinh-doanh)
- [Đề xuất tính năng & A/B Testing](#đề-xuất-tính-năng--ab-testing)
- [Công cụ sử dụng](#công-cụ-sử-dụng)
- [Cách chạy dự án](#cách-chạy-dự-án)
- [Dashboard](#dashboard)

---

## Bối cảnh dự án
**Scenario (Giả định):** Hãy tưởng tượng bạn là Data Analyst tại một Digital Bank (Ngân hàng số) hoặc ứng dụng FinTech hướng tới thị trường Mỹ. **Phòng Phát triển Sản phẩm (Product Team)** đang muốn cải tổ lại tính năng Quản lý chi tiêu cá nhân (PFM - Personal Financial Management) trên app (giống như tính năng quản lý chi tiêu của MoMo hay ngân hàng, nhưng làm sao để người dùng thực sự xài nó thay vì bỏ xó vì lười phân loại).

Để hiểu người dùng và nỗi đau (pain points) của họ, team cần phân tích dữ liệu. Tuy nhiên, kết quả khảo sát ban đầu bị thiếu hụt dữ liệu giao dịch ở quy mô lớn. Để giải quyết, **chúng tôi đã giả lập một bộ dữ liệu mô phỏng cực kỳ sát thực tế gồm 20.000 người dùng**, dựa trên thống kê vĩ mô của Mỹ.

Dashboard Tableau này được thiết kế để báo cáo cho **Product Manager và Growth Team**, giúp họ nhìn thấy bức tranh toàn cảnh: Nhóm nhân khẩu học nào đang gặp khó khăn tài chính, vì sao, và app cần xây dựng tính năng gì tiếp theo để giải cứu họ.

---

## Cách chúng tôi mô phỏng dữ liệu

Nếu chỉ dùng hàm random để sinh ngẫu nhiên các khoản chi tiêu sẽ làm mất đi tính logic thực tế (ví dụ: người trả tiền thuê nhà đắt tiền thường có chi phí sinh hoạt khác). Để dữ liệu sát với đời thực nhất, chúng tôi áp dụng **phân phối chuẩn đa biến (multivariate normal distribution)** để giữ nguyên tỷ lệ tương quan giữa các danh mục:

1. **Dữ kiện nền (CSV):** Bắt đầu với ~20.000 hồ sơ khảo sát cơ bản.
2. **Ma trận tương quan (XLSX):** Thu thập dữ liệu từ Cục Thống kê Lao động Mỹ (BLS.gov), làm sạch và tính toán **ma trận tương quan (correlation matrix)** cho các mục chi tiêu theo từng nhóm tuổi.
3. **Mô phỏng (Python):** Bơm dữ liệu qua mô hình log-transform và phân phối chuẩn đa biến để sinh ra các vector chi tiêu cuối cùng. Dữ liệu thành phẩm không chỉ khớp về mặt phân phối mà còn giữ được các quan hệ tuyến tính giống hệt thực tế.

*Tài liệu tham khảo:*
- **BaoCao_phu_Nhom_10.pdf** — Giải thích toán học về cách tạo dữ liệu.
- **Synthetic_data_generation.ipynb** — Code Python thực thi dữ liệu.

---

## Insight quan trọng & Giá trị kinh doanh

Chạy phân tích trên 20.000 user giả lập, chúng tôi tìm ra các insight cực kỳ định hướng cho Product Team:

| Nhóm tuổi | Tỷ lệ tiết kiệm | Thực tế tài chính |
|-----------|-----------------|---------|
| 18–25 | **–26.9%** | Âm tiền, tiêu nhiều hơn kiếm |
| 26–35 | +15.6% | Bắt đầu tích lũy, ổn định |
| 36–45 | **+28.7%** | Giai đoạn vàng, tiết kiệm tốt nhất |
| 46–55 | +1.9% | Gần bằng 0 (khả năng do chi phí nuôi con/y tế cao) |
| 56–65 | –86.6% | Rút tiền hưu trí để tiêu |

**Phát hiện đắt giá nhất cho team làm App:**
Chi tiêu không thiết yếu (ăn ngoài, giải trí, linh tinh) chỉ chiếm đúng **~8%** tổng chi tiêu của tất cả các nhóm tuổi.

> **Hàm ý cho sản phẩm:** Gen Z (18-25) âm tiền không phải vì họ uống trà sữa hay mua sắm quá nhiều, mà vì **chi phí cố định (thuê nhà, bảo hiểm, đi lại) đã nuốt sạch thu nhập ngay từ đầu tháng**. Nếu App chỉ chăm chăm hiện biểu đồ khuyên "Bạn bớt ăn ngoài đi" thì tính năng đó hoàn toàn vô dụng. Họ cần một giải pháp khác.

---

## Đề xuất tính năng & A/B Testing

Từ bức tranh toàn cảnh (Macro) ở trên, đây là đề xuất cụ thể đưa xuống cấp độ sản phẩm (Micro feature) để Product Team phát triển:

### Thử nghiệm A/B: Cảnh báo ngân sách "sống còn" (Proactive Pacing Alerts)

**Vấn đề:** Các app ngân hàng hoặc ví điện tử hiện tại thường báo cáo theo dạng bị động (reactive) – cuối tháng mới vẽ biểu đồ báo "Bạn đã tiêu lõm quỹ". Với nhóm 18-25 bị chi phí cố định bào mòn ngay từ đầu tháng, cái họ cần là cảnh báo chủ động (proactive).

**Tính năng đề xuất:** App tự động nhận diện các khoản phí cố định đầu tháng, trừ thẳng vào thu nhập, và chia đều số tiền ít ỏi còn lại cho những ngày cuối tháng kèm cảnh báo.

| | Nhóm A (Hiện tại) | Nhóm B (Thử nghiệm) |
|---|---|---|
| Trải nghiệm | Xem lại biểu đồ hình tròn cuối tháng. Tính năng tự động phân loại giao dịch (mà user hay phớt lờ). | Nhận Push Notification cảnh báo tốc độ tiêu tiền ngay giữa tháng. |
| Ví dụ | "Tháng này bạn đã tiêu 20 triệu vào Ăn uống & Sinh hoạt." | "Tiền nhà vừa trừ xong. Cảnh báo: Bạn chỉ còn 3 triệu cho 15 ngày tới. Phanh lại ngay!" |

**Giả thuyết (Hypothesis):** Bằng cách chuyển từ báo cáo "hậu kiểm" sang cảnh báo "tiền trạm", Nhóm B sẽ cải thiện tỷ lệ tiết kiệm (savings rate) trung bình cuối tháng tốt hơn Nhóm A.

#### Kết quả mô phỏng (từ `analyze_pf.py`)

- **Tỷ lệ tiết kiệm nhóm Đối chứng (Control):** -26.86%
- **Tỷ lệ tiết kiệm nhóm Thử nghiệm (Variation):** -14.18%
- **Chỉ số cải thiện (Lift):** **+12.69%**

**[INSIGHT]** Đối với nhóm 18-25, giải pháp 'Budget Alerts' giúp cải thiện đáng kể tình trạng tài chính, giảm mức thâm hụt hàng tháng tới gần một nửa. Điều này chứng minh giá trị của việc dùng Insight vĩ mô để thiết kế giải pháp sản phẩm vi mô cực kỳ hiệu quả.

---

## Công cụ sử dụng

| Công cụ | Dùng để làm gì |
|---------|---------------|
| Python (Pandas, NumPy, SciPy) | Xây dựng thuật toán, làm sạch và sinh dữ liệu mô phỏng |
| Tableau | Vẽ Dashboard báo cáo tổng quan chiến lược cho các bên liên quan (Stakeholders) |
| Nguồn Dữ Liệu | Cục Thống kê Lao động Mỹ (BLS.gov) |

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

---

## Dashboard

**Income Spending and Saving Overview.twbx** — Dashboard vĩ mô phân tích hành vi nhân khẩu học.

![Tổng Quan Nhóm Nhân Khẩu Học](Images/demographic.png)
[→ Xem Dashboard Tổng Quan trên Tableau Public](https://public.tableau.com/app/profile/nguy.n.phan.ho.ng.ph.c/viz/Book1_17516920190310/General?publish=yes)
