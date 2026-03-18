# Bảng Điều Khiển Tài Chính Cá Nhân (Tableau)



## Mục Lục
- [Tổng Quan Dự Án](#tổng-quan-dự-án)
- [Những Bài Học Cốt Lõi](#những-bài-học-cốt-lõi)
- [Bối Cảnh](#bối-cảnh)
- [Phương Pháp Luận (Khung STAR)](#phương-pháp-luận-khung-star)
- [Những Phát Hiện Chính](#những-phát-hiện-chính)
- [Công Cụ & Kỹ Năng](#công-cụ--kỹ-năng)
- [Hướng Phát Triển Tiếp Theo](#hướng-phát-triển-tiếp-theo)
- [Bắt Đầu Dự Án](#bắt-đầu-dự-án)
  - [Cách Clone Dự Án](#cách-clone-dự-án)
  - [Cách Cài Đặt Dự Án](#cách-cài-đặt-dự-án)
- [Ảnh Chụp Màn Hình](#ảnh-chụp-màn-hình)

---

## Tổng Quan Dự Án
[Read in English](README.md)

Dự án này phân tích các dữ liệu tài chính cá nhân mô phỏng nhằm tìm hiểu các xu hướng về thu nhập, chi tiêu và tiết kiệm ở các nhóm nhân khẩu học khác nhau theo thời gian. Dự án bao gồm cả quá trình tạo dữ liệu mô phỏng và giai đoạn trực quan hóa dữ liệu bằng Tableau.

Để hiểu toàn bộ dự án, vui lòng tham khảo theo thứ tự sau:

1. **BaoCao_phu_Nhom_10.pdf** - Giải thích cách dữ liệu được điều chỉnh và tạo ra.
2. **Synthetic_data_generation.ipynb** - Notebook mô tả quá trình tạo dữ liệu mô phỏng (lấy mẫu, thêm nhiễu, xác thực).
3. **BaoCao_Nhom_10.pdf** - Báo cáo phân tích chính tổng hợp quy trình làm việc, thiết kế bảng điều khiển và các thông tin chi tiết.
4. **Income Spending and Saving Overview.twbx** - Bảng điều khiển Tableau trực quan hóa hành vi tài chính ở cấp độ tổng thể dân số.
5. **Actual Spending Behavior Analysis.twbx** - Bảng điều khiển Tableau phân tích chi tiết hành vi chi tiêu và tiết kiệm của cá nhân.

Cấu trúc thư mục:
```text
nhom_10
├── Reports/
│   ├── main_report.pdf
│   └── other_report.pdf
│
├── Notebooks/
│   ├── Datacleaned_Nhom_10.ipynb
│   └── Synthetic_data_generation.ipynb
│
├── Dashboards/
│   ├── Income Spending and Saving Overview.twbx
│   └── Actual Spending Behavior Analysis.twbx
│
└── Data/
    ├── synthetic_data_output.csv
    ├── [1] Personal_Finance_Dataset.csv
    ├── [1] financial-literacy-data.csv
    └── reference-person-age-ranges-2023.xlsx
```

## Những Bài Học Cốt Lõi

- **Quy Trình Xử Lý Dữ Liệu Toàn Diện:** Có được sự hiểu biết sâu sắc về quá trình tạo lập, thêm nhiễu thống kê và kiểm tra xác thực dữ liệu mô phỏng thông qua Python.
- **Kỹ Năng Trực Quan Hóa Cấp Cao:** Phát triển kỹ năng xây dựng bảng điều khiển có tính tương tác cao trên Tableau để truyền tải các chỉ số tài chính phức tạp đến với nhiều đối tượng người xem.
- **Phân Tích Hành Vi:** Nâng cao tư duy phân tích thông qua việc xác định và mổ xẻ các khuôn mẫu chi tiêu dựa trên nhân khẩu học nhằm rút ra những kiến thức có tính ứng dụng thực tiễn.
- **Giao Tiếp Trong Công Việc:** Cải thiện kỹ năng kể chuyện bằng dữ liệu (Data Storytelling) qua việc trình bày các báo cáo phân tích một cách có cấu trúc và chi tiết.

## Bối Cảnh

Dự án mô phỏng hiểu biết tài chính và hành vi tài chính cá nhân nhằm mục đích:
- Xác định những khác biệt về nhân khẩu học trong tiềm năng thu nhập và tiết kiệm.
- Phát hiện các kiểu chi tiêu kém hiệu quả và đưa ra gợi ý cải thiện.
- Chứng minh cách trực quan hóa dựa trên dữ liệu có thể hỗ trợ việc ra quyết định tài chính.

## Phương Pháp Luận (Khung STAR)

### Tình Huống (Situation)
Cần phân tích hai tập dữ liệu mô phỏng đại diện cho hoạt động tài chính ở cấp độ tổng thể dân số và cấp độ cá nhân.

### Nhiệm Vụ (Task)
Xây dựng các bảng điều khiển Tableau tương tác để trực quan hóa xu hướng chi tiêu - tiết kiệm, đồng thời cung cấp các kết luận có giá trị ứng dụng.

### Hành Động (Action)
- Tạo và xác thực dữ liệu mô phỏng bằng Python.
- Xử lý sạch và định dạng cấu trúc dữ liệu (20.000 dòng và 1.500 dòng).
- Thiết lập bảng điều khiển với các thẻ KPI, bản đồ nhiệt và phân tích xu hướng trên Tableau.
- Đối chiếu những phát hiện ở cấp độ nhân khẩu học chung và cấp độ cá nhân để tìm ra các mô hình hành vi.

### Kết Quả (Result)
- Tạo thành công hai bảng điều khiển tương tác tóm tắt các chỉ số chính:
  - Thu nhập trung bình: 74.503 USD, Chi tiêu: 66.196 USD, Tiết kiệm: 8.307 USD (11%).
- Xác định "Di chuyển & Bảo hiểm" (Transport & Insurance) là các nguồn chi phí lớn nhất.
- Phát hiện chi tiêu không thiết yếu chiếm tới 58% tổng chi phí trong tập dữ liệu cá nhân.
- Đề xuất các chiến lược để nâng cao thói quen tiết kiệm và tối ưu hóa các khoản mục chi tiêu.

## Những Phát Hiện Chính

| Hạng Mục | Quan Sát | Ý Nghĩa Thực Tiễn |
|-----------|--------------|--------------|
| **Độ Tuổi 18–25** | Tỷ lệ tiết kiệm thấp nhất | Cần sớm được giáo dục về tài chính |
| **Di Chuyển & Bảo Hiểm** | Dẫn đầu các danh mục chi tiêu | Có tiềm năng tối ưu hóa để tiết kiệm |
| **Chi Tiêu Không Thiết Yếu (58%)** | Tăng trưởng nhanh hơn thu nhập | Cần khuyến khích ngân sách tự động |

## Công Cụ & Kỹ Năng

- **Python (Pandas, NumPy)** - Phương pháp tạo dữ liệu mô phỏng
- **Tableau** - Thiết kế bảng điều khiển, trực quan hóa KPI
- **Excel / Google Sheets** - Xử lý dọn dẹp và xác thực dữ liệu
- **Data Storytelling** - Truyền đạt thông tin chi tiết và viết báo cáo

## Hướng Phát Triển Tiếp Theo

- **Tích Hợp Dữ Liệu Theo Thời Gian Thực:** Kết nối vào các API tài chính cá nhân hoặc xuất tệp từ ngân hàng để phân tích dữ liệu sống.
- **Phân Tích Dự Đoán:** Ứng dụng mô hình học máy (Machine Learning) để dự đoán chi tiêu trong tương lai và ước lượng tỷ lệ tiết kiệm dựa theo xu hướng hiện tại.
- **Tăng Cường Tính Cá Nhân Hóa:** Thêm vào bảng điều khiển Tableau các phần tùy chỉnh cho từng mục tiêu tài chính cụ thể.
- **Tự Động Hóa Xử Lý Dữ Liệu:** Cải tiến lại các file Python sang một luồng dữ liệu (Data Pipeline) tự động thông qua các công cụ lên lịch quy trình làm việc.

## Bắt Đầu Dự Án

### Cách Clone Dự Án

Khởi chạy lệnh sau trong terminal của bạn để sao chép (clone) kho lưu trữ mã nguồn này về máy:

```bash
git clone https://github.com/hoangf384/pf-visualization.git
cd pf-visualization
```
*(Thay thế `hoangf384/pf-visualization` bằng URL chính xác của dự án nếu cần).*

### Cách Cài Đặt Dự Án

Thực hiện các bước sau để thiết lập môi trường phát triển cần thiết, dùng cho việc khởi chạy các Notebook Python:

```bash
# 1. Tạo môi trường ảo (virtual environment)
python -m venv .venv

# 2. Kích hoạt môi trường ảo
# Đối với Windows:
.venv\Scripts\activate
# Đối với macOS/Linux:
source .venv/bin/activate

# 3. Cài đặt các thư viện Python bổ trợ
pip install -r requirements.txt

# 4. Đăng ký kernel Python của môi trường ảo vào Jupyter
python -m ipykernel install --user --name=.venv --display-name "Python (.venv)"
```

Khi bạn đã hoàn thành bước thứ tư, kernel tùy chỉnh này đã được thiết lập. Mỗi khi mở Jupyter Notebook (`.ipynb`), hãy chọn tới kernel `Python (.venv)` để có thể chạy các thư viện trong một môi trường được cô lập hoàn toàn.

## Ảnh Chụp Màn Hình

![Tổng Quan Nhóm Nhân Khẩu Học](images/demographic.png)  
[Xem Bảng Điều Khiển Tổng Quan](https://public.tableau.com/app/profile/nguy.n.phan.ho.ng.ph.c/viz/Book1_17516920190310/General?publish=yes)

![Hành Vi Chi Tiêu](images/Behaviors.png)  
[Xem Phân Tích Hành Vi Chi Tiêu](https://public.tableau.com/app/profile/nguyen.nhi8170/viz/CuoiKy_17519870918010/Dashboard1?publish=yes)
