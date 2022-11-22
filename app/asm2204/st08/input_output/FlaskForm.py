class FlaskForm:
    input_dict = {}
    output_list = []

    def __init__(self):
        pass

    def input(self, form_dict):
        self.input_dict = form_dict

    def get_input_data(self):
        return self.input_dict

    def clear_for_output(self):
        self.output_list = []

    def add_for_output(self, field_name_list, value_list):
        self.output_list.append(dict(zip(field_name_list,  value_list)))

    def output(self):
        return self.output_list
