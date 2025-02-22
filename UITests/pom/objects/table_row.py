from playwright.sync_api import Page, Locator

class TableRow:
    def __init__(self, page: Page, row_locator: Locator):
        self.page = page
        self.row_locator = row_locator  # The locator specific to this row

        self.cells = row_locator.locator('td')
        self.edit_employee_button = row_locator.locator('i.fa-edit')
        self.delete_employee_button = row_locator.locator('i.fa-times')

    def get_column_value_by_index(self, index: int) -> str:
        # Get the specific cell by index and return its text content
        return self.cells.nth(index).inner_text()