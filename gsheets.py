import os.path as path
from googleapiclient.discovery import build
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1FSMATLJUNCbV8-XYM8h7yHoWRSGA8JFsaECOZy_i2T8'


def main():
    service_account_json = path.join(path.dirname(
        path.abspath(__file__)), 'service_account.json')
    credentials = service_account.Credentials.from_service_account_file(
        service_account_json, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    sheet_service = service.spreadsheets()

    print('Getting pie chart information')
    get_pie_chart_info(sheet_service)

    print('Getting line chart information')
    get_line_chart_info(sheet_service)

    print('Getting boolean information')
    get_bool_info(sheet_service)


def get_pie_chart_info(sheet_service):
    sample_range_name = 'data!F:G'
    result = sheet_service.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=sample_range_name).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Race, Breakdown:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))


def get_line_chart_info(sheet_service):
    sample_range_name = 'data!D:D'
    result = sheet_service.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=sample_range_name).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Time series information:')
        for row in values:
            print('%s' % row[0])


def get_bool_info(sheet_service):
    sample_range_name = 'data!B1'
    result = sheet_service.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=sample_range_name).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Time series information:')
        for row in values:
            print(row[0] == 'TRUE')


if __name__ == '__main__':
    main()
