# python
Chapter 6 - Regular Expression:
Mục tiêu chính:
- Xây dựng chương trình biểu thức chính qui để kiểm tra dữ liệu (validation)

Để tránh nhầm lẫn khi làm việc với regular expression, ta sẽ sử dụng Raw String như r'expression'
-- Các pattern đơn giản match với kí tự đơn:
. : khớp với các ký tự đơn trừ ký tự dòng mới newline '\n'
\w : khớp với word character (a-zA-Z0-9_) 
\W : khớp với non-word character
\s : khớp với single white character
\S : khớp với non-whitespace character
\t,\n,\r : tab, newline, return
\d : decimal digit [0-9]
^ : khớp với bắt đầu chuồi
$ : khớp với cuối chuỗi
\ : đứng trước ký tự như các mô tả trên 

Bài tập:
1. kiem_tra_chuoi_ki_tu.py
2. kiem_tra_match.py
3. kiem_tra_chuoi_thuong.py
4. kiem_tra_chuoi_a_b.py
5. tim_chuoi_con_trong_chuoi.py
