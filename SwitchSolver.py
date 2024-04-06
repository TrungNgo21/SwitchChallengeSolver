class SwitchSolver:
    branches_lst = []
    top_layer = []
    bottom_layer = []

    def __init__(self, branches_lst, top_layer, bottom_layer):
        self.top_layer = top_layer
        self.bottom_layer = bottom_layer
        self.branches_lst = self.generate_branches(branches_lst)

    def generate_branches(self, input_list):
        # Tìm số lượng các list con
        num_sublists = len(input_list)

        # Kiểm tra nếu không có list con, trả về một list rỗng
        if num_sublists == 0:
            return []

        # Tính toán tất cả các kết hợp của các phần tử từ các list con
        def generate_recursive(index):
            if index == num_sublists:
                return [[]]

            results = []
            for value in input_list[index]:
                for subresult in generate_recursive(index + 1):
                    results.append([value] + subresult)
            return results

        # Bắt đầu đệ quy từ index 0
        return generate_recursive(0)

    def shuffle(self, shape_layer, node):
        converted = []
        for number in str(node):
            if number == '1':
                converted.append(shape_layer[0])
            elif number == '2':
                converted.append(shape_layer[1])
            elif number == '3':
                converted.append(shape_layer[2])
            else:
                converted.append(shape_layer[3])
        return converted

    def choose_branch(self):
        for branch in self.branches_lst:
            begin = self.top_layer.copy()
            for node in branch:
                begin = self.shuffle(begin, node)
            if begin == self.bottom_layer:
                return branch
