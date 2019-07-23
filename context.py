# coding=utf-8
from branch import Branch
import pandas


class Context():
    def __init__(self, name):
        self.name = name
        self.branches = []
        self.current_branch = None

    def add_branch(self, branch):
        self.branches.append(branch)
        if self.current_branch is None:
            self.current_branch = branch

    def move_to_next_branch(self, intent):
        self.current_branch = self.current_branch.get_next_branch(intent)


welcome_context = Context('preCol')
root_branch = Branch(0, '', '')
welcome_context.add_branch(root_branch)


# layer 1
nhanh_co_1 = Branch(1, 'co', 'Có')
nhanh_khong_muon_nghe = Branch(1, "khong_muon_nghe", "Không muốn nghe")
nhanh_khong = Branch(1, 'khong', "Không")
root_branch.add_next_branch(nhanh_co_1)
root_branch.add_next_branch(nhanh_khong_muon_nghe)
root_branch.add_next_branch(nhanh_khong)


# layer 1.1
nhanh_co_2_1 = Branch(1.5, 'co', "Có")
nhanh_khong_quen_2_1 = Branch(1.5, 'khong_quen', "Không quen")
nhanh_cua_hang = Branch(1.5, "cua_hang", "Cửa hàng")

nhanh_khong.add_next_branch(nhanh_co_2_1)
nhanh_khong.add_next_branch(nhanh_khong_quen_2_1)
nhanh_khong.add_next_branch(nhanh_cua_hang)


# layer 2
nhanh_co_1_1 = Branch(2, 'co', "Có")
nhanh_co_1.add_next_branch(nhanh_co_1_1)


# layer 5
nhanh_binh_thuong = Branch(5, 'binh_thuong', "Bình thường")
nhanh_rat_hai_long = Branch(5, 'rat_hai_long', "Rất hài lòng")
nhanh_rat_khong_hai_long = Branch(5, 'rat_khong_hai_long', "Rất không hài lòng")
nhanh_hai_long = Branch(5, 'hai_long', "Hài lòng")
nhanh_khong_hai_long = Branch(5, 'khong_hai_long', "Không hài lòng")

nhanh_co_1_1.add_next_branch(nhanh_binh_thuong)
nhanh_co_1_1.add_next_branch(nhanh_rat_hai_long)
nhanh_co_1_1.add_next_branch(nhanh_rat_khong_hai_long)
nhanh_co_1_1.add_next_branch(nhanh_hai_long)
nhanh_co_1_1.add_next_branch(nhanh_khong_hai_long)


# layer 6
nhanh_co_1_1_1 = Branch(6, 'co', "Có")
nhanh_khong_1_1_1 = Branch(6, 'khong', "Không")
nhanh_khong_nho_khong_biet_1_1_1 = Branch(6, 'khong_nho', "Không nhớ, không biết")

for branch in nhanh_co_1_1.next_branches:
    branch.add_next_branch(nhanh_co_1_1_1)
    branch.add_next_branch(nhanh_khong_1_1_1)
    branch.add_next_branch(nhanh_khong_nho_khong_biet_1_1_1)


# layer 7
nhanh_tb_gia_dinh = Branch(7, 'trang_thiet_bi_gia_dinh', "Trang thiết bị gia đình")
nhanh_van_hoa = Branch(7, 'chi_phi_van_hoa', "Chi phí văn hóa")
nhanh_phuong_tien = Branch(7, 'phuong_tien', "Mua phương tiện đi lại")
nhanh_du_lich = Branch(7, 'du_lich', "Chi phí du lịch")
nhanh_khach_hang_khong_hop_tac = Branch(7, 'khong_hop_tac', "Khách hàng không hợp tác")
nhanh_sua_chua_nha_o = Branch(7, 'sua_chua_nha', "Chi phí sửa chữa nhà ở")
nhanh_the_thao = Branch(7, 'the_thao', "Chi phí thể thao")
nhanh_hoc_tap = Branch(7, 'hoc_tap', "Chi phí học tập")
nhanh_chua_benh = Branch(7, 'chua_benh', "Chi phí chữa bệnh")
nhanh_do_dung = Branch(7, 'do_dung', "Mua đồ dùng")

nhanh_co_1_1_1.add_next_branch(nhanh_tb_gia_dinh)
nhanh_co_1_1_1.add_next_branch(nhanh_van_hoa)
nhanh_co_1_1_1.add_next_branch(nhanh_phuong_tien)
nhanh_co_1_1_1.add_next_branch(nhanh_du_lich)
nhanh_co_1_1_1.add_next_branch(nhanh_khach_hang_khong_hop_tac)
nhanh_co_1_1_1.add_next_branch(nhanh_sua_chua_nha_o)
nhanh_co_1_1_1.add_next_branch(nhanh_the_thao)
nhanh_co_1_1_1.add_next_branch(nhanh_hoc_tap)
nhanh_co_1_1_1.add_next_branch(nhanh_chua_benh)
nhanh_co_1_1_1.add_next_branch(nhanh_do_dung)


# layer 8
nhanh_co_1_1_1_1 = Branch(8, 'co', "Có")
nhanh_khong_1_1_1_1 = Branch(8, 'khong', "Không")
for branch in nhanh_co_1_1_1.next_branches:
    branch.add_next_branch(nhanh_co_1_1_1_1)
    branch.add_next_branch(nhanh_khong_1_1_1_1)

# basic info
no = []
tels = []
names = []
genders = []
products = []
amounts = []
due_dates = []
contract_nums = []

# Welcome call info
call_starts_welcome = []
pickup = []
pickup_times = []
hangup_times = []
hangup_steps = []


def calculate_hangup_steps(data):
    answers = data.split('/')
    print len(answers)


path = ('Master.csv')
df = pandas.read_csv(path, header=None)
df.fillna("", inplace=True)
for i in range(len(df)):
    data = df.loc[i]
    for col in data:
        no.append(i)
        tels.append(data[0])
        names.append(data[1])
        genders.append(data[2])
        products.append(data[3])
        amounts.append(data[4])
        due_dates.append(data[5])
        contract_nums.append(data[6])
        call_starts_welcome.append(data[7])
        pickup.append(data[8])
        pickup_times.append(data[9])
        hangup_times.append(data[10])
        hangup_steps.append(calculate_hangup_steps(data[11]))
