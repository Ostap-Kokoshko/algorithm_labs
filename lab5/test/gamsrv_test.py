import unittest
import os

from lab5.src.gamsrv import read_input_file, gamsrv, write_output_file


class TestGAMSRV(unittest.TestCase):

    def test_case_1(self):
        input_file_path = 'gamsrv_1.in'
        output_file_path = 'gamsrv_1.out'

        with open(input_file_path, 'w') as file:
            file.write("6 6 \n "
                       "1 2 6 \n"
                       "1 3 10 \n"
                       "3 4 80 \n"
                       "4 5 50 \n"
                       "5 6 20 \n"
                       "2 3 40 \n"
                       "2 4 100 \n")

        expected_output = "100"

        graph, client_list = read_input_file(input_file_path)
        result = gamsrv(graph, client_list)
        write_output_file(output_file_path, result)

        with open(output_file_path, 'r') as file:
            actual_output = file.read().strip()

        self.assertEqual(actual_output, expected_output)

        os.remove(input_file_path)
        os.remove(output_file_path)

    def test_case_2(self):
        input_file_path = 'gamsrv_2.in'
        output_file_path = 'gamsrv_2.out'

        with open(input_file_path, 'w') as file:
            file.write(
                "9 12 \n"
                "2 4 6 \n"
                "1 2 20 \n"
                "2 3 20 \n"
                "3 6 20 \n"
                "6 9 20 \n"
                "9 8 20 \n"
                "8 7 20 \n"
                "7 4 20 \n"
                "4 1 20 \n"
                "5 2 10 \n"
                "5 4 10 \n"
                "5 6 10 \n"
                "5 8 10 \n")

        expected_output = "10"

        graph, client_list = read_input_file(input_file_path)
        result = gamsrv(graph, client_list)
        write_output_file(output_file_path, result)

        with open(output_file_path, 'r') as file:
            actual_output = file.read().strip()

        self.assertEqual(actual_output, expected_output)

        os.remove(input_file_path)
        os.remove(output_file_path)

    def test_case_3(self):
        input_file_path = 'gamsrv_3.in'
        output_file_path = 'gamsrv_3.out'

        with open(input_file_path, 'w') as file:
            file.write("3 2 \n"
                       "1 3 \n"
                       "1 2 50 \n"
                       "2 3 1000000000 \n")

        expected_output = "1000000000"

        graph, client_list = read_input_file(input_file_path)
        result = gamsrv(graph, client_list)
        write_output_file(output_file_path, result)

        with open(output_file_path, 'r') as file:
            actual_output = file.read().strip()

        self.assertEqual(actual_output, expected_output)
        os.remove(input_file_path)
        os.remove(output_file_path)


if __name__ == '__main__':
    unittest.main()
