import time
from playwright.sync_api import Page

from pom.objects.table_row import TableRow

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = self.page.locator("h1.dashboard-title")
        self.table = self.page.locator('//*[@id="employeesTable"]')
        self.table_header = self.table.locator('//thead[@class="thead-dark"]/tr/th')
        self.table_row = self.table.locator("//tbody/tr")
        self.add_employee_button = self.page.locator('//*[@id="add"]')
        self.log_out_link = self.page.locator('a[href="/Prod/Account/LogOut"]')
        self.footer = self.page.locator('footer[class="footer"]')

    def get_title(self):
        return self.title.inner_text()

    def get_row(self, index: int) -> TableRow:
        # Get a specific row by index
        row_locator = self.table_row.nth(index)
        return TableRow(self.page, row_locator)  # Return a TableRow object with the locator
    
    def get_table_rows_count(self) -> int:
        return self.table_row.count()

    def get_table_header_texts(self) -> list:
        header_elements = self.table_header.all()
        return [header.inner_text() for header in header_elements]
    
    def get_header_index_by_text(self, header_text: str) -> int:
        # Get the index of the header with specific text
        headers = self.get_table_header_texts()
        try:
            return headers.index(header_text)
        except ValueError:
            return -1
        
    def get_table_row_by_full_employee_name(self, first_name: str, last_name: str) -> TableRow:
        # Get all rows in the table
        rows_count = self.get_table_rows_count()

        # Get column indices for First Name and Last Name
        first_name_value_index = self.get_header_index_by_text("First Name")
        last_name_value_index = self.get_header_index_by_text("Last Name")
        
        for index in range(rows_count):
            # Get the row object by index
            row = self.get_row(index)
            
            first_name_value = row.get_column_value_by_index(first_name_value_index)
            last_name_value = row.get_column_value_by_index(last_name_value_index)
            
            # Check if both values match the given criteria
            if first_name_value == first_name and last_name_value == last_name:
                return row  # Return the matching row
            
    def get_table_row_by_id(self, id: str) -> TableRow:
        # Get all rows in the table
        rows_count = self.get_table_rows_count()

        id_value_index = self.get_header_index_by_text("Id")
        
        for index in range(rows_count):
            # Get the row object by index
            row = self.get_row(index)
            
            id_value = row.get_column_value_by_index(id_value_index)
            
            if id_value == id:
                return row  # Return the matching row
            
    def get_column_value_in_the_row(self, row: TableRow, column_name: str) -> str:
        value_index = self.get_header_index_by_text(column_name)
        return row.get_column_value_by_index(value_index)

    def wait_for_table_to_be_loaded(self):
        # I didn't find a simple solution to wait until the table is reloaded after any changes
        # There is no table spinner to rely on it. It's possible to wait for API responses to get 200 OK, but it's seems too complex for this
        # For now I will leave this implicit wait, but definetly it's a bad solution
        time.sleep(2)