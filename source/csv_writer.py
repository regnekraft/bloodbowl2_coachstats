import csv

class Csv_writer:

    def create_csv(self, csv_file_path, csv_filename, header_row_list, list_with_rows):
        with open(csv_file_path + csv_filename, 'w', newline='', encoding='iso-8859-1') as file:
            writer = csv.writer(file, delimiter=";")
            #writer.writerow(['uuid', 'fullname'])
            writer.writerow(header_row_list)
            for row in list_with_rows:
                # writer.writerow([am.uuid_userref, am.name])
                writer.writerow(row)
