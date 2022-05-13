import requests
import json
import os
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from prettytable import PrettyTable
from email.mime.text import MIMEText
from dining_location import location


truegrit_user = os.environ.get("TRUEGRIT_USER")
truegrit_pass = os.environ.get("TRUEGRIT_PASS")

# customer_list = ["tlostos1@umbc.edu",
#                  "nnegi1@umbc.edu",
#                  "r148@umbc.edu",
#                  "zhoward1@umbc.edu"]
customer_list = ["il27770@umbc.edu"]

print(truegrit_user)
print(truegrit_pass)

with smtplib.SMTP("smtp.gmail.com", 587) as stmp:
    stmp.ehlo()
    stmp.starttls()
    stmp.ehlo()

    stmp.login(truegrit_user, truegrit_pass)

    truegrits_location_id = '61f9d7c8a9f13a15d7c1a25e'

    date = str(date.today())
    # date = "2022-05-05"
    url = 'https://api.dineoncampus.com/v1/location/61f9d7c8a9f13a15d7c1a25e/periods/?platform=0&date=' + date
    init_response = requests.get(url)
    json_data = json.loads(init_response.text)
    location("UMBC", 'https://api.dineoncampus.com/v1/location/61f9d7c8a9f13a15d7c1a25e/periods/?platform=0&date=', date)


    tabular_fields = ["Meal Period", "Category", "Items"]
    tabular_table = PrettyTable()
    tabular_table.field_names = tabular_fields

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Today's Menu: " + date
    msg['From'] = truegrit_user
    msg['To'] = customer_list[0]
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    # html = """\
    # <html>
    #   <head></head>
    #   <body>
    #     <p>Hi!<br>
    #        How are you?<br>
    #        Here is the <a href="http://www.python.org">link</a> you wanted.
    #     </p>
    #   </body>
    # </html>
    # """

    html = """\
    <!DOCTYPE html PUBLI>
    <html
      xmlns="http://www.w3.org/1999/xhtml"
      xmlns:v="urn:schemas-microsoft-com:vml"
      xmlns:o="urn:schemas-microsoft-com:office:office"
    >
      <head>
        <!--[if gte mso 9]>
          <xml>
            <o:OfficeDocumentSettings>
              <o:AllowPNG />
              <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
          </xml>
        <![endif]-->

        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="x-apple-disable-message-reformatting" />

        <!--[if !mso]><!-->
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <!--<![endif]-->
        <title></title>

        <style type="text/css">
          @media only screen and (min-width: 520px) {
            .u-row {
              width: 500px !important;
            }
            .u-row .u-col {
              vertical-align: top;
            }

            .u-row .u-col-100 {
              width: 500px !important;
            }
          }

          @media (max-width: 520px) {
            .u-row-container {
              max-width: 100% !important;
              padding-left: 0px !important;
              padding-right: 0px !important;
            }
            .u-row .u-col {
              min-width: 320px !important;
              max-width: 100% !important;
              display: block !important;
            }
            .u-row {
              width: calc(100% - 40px) !important;
            }
            .u-col {
              width: 100% !important;
            }
            .u-col > div {
              margin: 0 auto;
            }
          }
          body {
            margin: 0;
            padding: 0;
          }

          table,
          tr,
          td {
            vertical-align: top;
            border-collapse: collapse;
          }

          .ie-container table,
          .mso-container table {
            table-layout: fixed;
          }

          * {
            line-height: inherit;
          }

          a[x-apple-data-detectors="true"] {
            color: inherit !important;
            text-decoration: none !important;
          }

          table,
          td {
            color: #000000;
          }
        </style>
      </head>

      <body
        class="clean-body u_body"
        style="
          margin: 0;
          padding: 0;
          -webkit-text-size-adjust: 100%;
          background-color: #e7e7e7;
          color: #000000;
        "
      >
        <!--[if IE]><div class="ie-container"><![endif]-->
        <!--[if mso]><div class="mso-container"><![endif]-->
        <table
          style="
            border-collapse: collapse;
            table-layout: fixed;
            border-spacing: 0;
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
            vertical-align: top;
            min-width: 320px;
            margin: 0 auto;
            background-color: #e7e7e7;
            width: 100%;
          "
          cellpadding="0"
          cellspacing="0"
        >
          <tbody>
            <tr style="vertical-align: top">
              <td
                style="
                  word-break: break-word;
                  border-collapse: collapse !important;
                  vertical-align: top;
                "
              >
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #e7e7e7;"><![endif]-->

                <div
                  class="u-row-container"
                  style="padding: 0px; background-color: transparent"
                >
                  <div
                    class="u-row"
                    style="
                      margin: 0 auto;
                      min-width: 320px;
                      max-width: 500px;
                      overflow-wrap: break-word;
                      word-wrap: break-word;
                      word-break: break-word;
                      background-color: transparent;
                    "
                  >
                    <div
                      style="
                        border-collapse: collapse;
                        display: table;
                        width: 100%;
                        background-color: transparent;
                      "
                    >
                      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->

                      <!--[if (mso)|(IE)]><td align="center" width="500" style="width: 500px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                      <div
                        class="u-col u-col-100"
                        style="
                          max-width: 320px;
                          min-width: 500px;
                          display: table-cell;
                          vertical-align: top;
                        "
                      >
                        <div style="width: 100% !important">
                          <!--[if (!mso)&(!IE)]><!--><div
                            style="
                              padding: 0px;
                              border-top: 0px solid transparent;
                              border-left: 0px solid transparent;
                              border-right: 0px solid transparent;
                              border-bottom: 0px solid transparent;
                            "
                          ><!--<![endif]-->
                            <table
                              style="font-family: arial, helvetica, sans-serif"
                              role="presentation"
                              cellpadding="0"
                              cellspacing="0"
                              width="100%"
                              border="0"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    style="
                                      overflow-wrap: break-word;
                                      word-break: break-word;
                                      padding: 10px;
                                      font-family: arial, helvetica, sans-serif;
                                    "
                                    align="left"
                                  >
                                    <table
                                      height="0px"
                                      align="center"
                                      border="0"
                                      cellpadding="0"
                                      cellspacing="0"
                                      width="100%"
                                      style="
                                        border-collapse: collapse;
                                        table-layout: fixed;
                                        border-spacing: 0;
                                        mso-table-lspace: 0pt;
                                        mso-table-rspace: 0pt;
                                        vertical-align: top;
                                        border-top: 1px solid #bbbbbb;
                                        -ms-text-size-adjust: 100%;
                                        -webkit-text-size-adjust: 100%;
                                      "
                                    >
                                      <tbody>
                                        <tr style="vertical-align: top">
                                          <td
                                            style="
                                              word-break: break-word;
                                              border-collapse: collapse !important;
                                              vertical-align: top;
                                              font-size: 0px;
                                              line-height: 0px;
                                              mso-line-height-rule: exactly;
                                              -ms-text-size-adjust: 100%;
                                              -webkit-text-size-adjust: 100%;
                                            "
                                          >
                                            <span>&#160;</span>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                  </td>
                                </tr>
                              </tbody>
                            </table>

                            <table
                              style="font-family: arial, helvetica, sans-serif"
                              role="presentation"
                              cellpadding="0"
                              cellspacing="0"
                              width="100%"
                              border="0"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    style="
                                      overflow-wrap: break-word;
                                      word-break: break-word;
                                      padding: 10px;
                                      font-family: arial, helvetica, sans-serif;
                                    "
                                    align="left"
                                  >
                                    <h1
                                      style="
                                        margin: 0px;
                                        line-height: 140%;
                                        text-align: center;
                                        word-wrap: break-word;
                                        font-weight: normal;
                                        font-family: arial, helvetica, sans-serif;
                                        font-size: 22px;
                                      "
                                    >
                                      Today's Menu
                                    </h1>
                                  </td>
                                </tr>
                              </tbody>
                            </table>

                            <table
                              style="font-family: arial, helvetica, sans-serif"
                              role="presentation"
                              cellpadding="0"
                              cellspacing="0"
                              width="100%"
                              border="0"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    style="
                                      overflow-wrap: break-word;
                                      word-break: break-word;
                                      padding: 10px;
                                      font-family: arial, helvetica, sans-serif;
                                    "
                                    align="left"
                                  >
                                    <table
                                      height="0px"
                                      align="center"
                                      border="0"
                                      cellpadding="0"
                                      cellspacing="0"
                                      width="100%"
                                      style="
                                        border-collapse: collapse;
                                        table-layout: fixed;
                                        border-spacing: 0;
                                        mso-table-lspace: 0pt;
                                        mso-table-rspace: 0pt;
                                        vertical-align: top;
                                        border-top: 1px solid #bbbbbb;
                                        -ms-text-size-adjust: 100%;
                                        -webkit-text-size-adjust: 100%;
                                      "
                                    >
                                      <tbody>
                                        <tr style="vertical-align: top">
                                          <td
                                            style="
                                              word-break: break-word;
                                              border-collapse: collapse !important;
                                              vertical-align: top;
                                              font-size: 0px;
                                              line-height: 0px;
                                              mso-line-height-rule: exactly;
                                              -ms-text-size-adjust: 100%;
                                              -webkit-text-size-adjust: 100%;
                                            "
                                          >
                                            <span>&#160;</span>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                  </td>
                                </tr>
                              </tbody>
                            </table>

                            <table
                              style="font-family: arial, helvetica, sans-serif"
                              role="presentation"
                              cellpadding="0"
                              cellspacing="0"
                              width="100%"
                              border="0"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    style="
                                      overflow-wrap: break-word;
                                      word-break: break-word;
                                      padding: 10px;
                                      font-family: arial, helvetica, sans-serif;
                                    "
                                    align="left"
                                  >
                                    <div>
                                      <div class="hscroll">
                                        <table
                                          width="100%"
                                          border="1"
                                          cellspacing="0"
                                          cellpadding="6"
                                        >

                                          REPLACE-HERE
                                        </table>
                                      </div>
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>

                            <!--[if (!mso)&(!IE)]><!-->
                          </div>
                          <!--<![endif]-->
                        </div>
                      </div>
                      <!--[if (mso)|(IE)]></td><![endif]-->
                      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                    </div>
                  </div>
                </div>

                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
              </td>
            </tr>
          </tbody>
        </table>
        <!--[if mso]></div><![endif]-->
        <!--[if IE]></div><![endif]-->
      </body>
    </html>
    
    """
    alt = """<tbody>
                <tr>
                  <th>Meal Period</th>
                  <th>Category</th>
                  <th>Item</th>
                </tr>
                <tr>
                  <td>Ron</td>
                  <td>Wilson</td>
                  <td>30</td>
                </tr>
                <tr>
                  <td>Armando</td>
                  <td>Reyes</td>
                  <td>17</td>
                </tr>
                <tr>
                  <td>Sarah</td>
                  <td>Thompkins</td>
                  <td>62</td>
                </tr>
                <tr>
                  <td>Lorraine</td>
                  <td>Schugel</td>
                  <td>25</td>
                </tr>
              </tbody>"""

    # html = html.replace("REPLACE-HERE", alt)


    list_mealperiod = []
    list_category = []

    meal_periods_dict = {}

    body_msg = ""
    data_period = json_data['periods']
    for period in data_period:
        meal_periods_dict[period["name"]] = period["id"]

    for period in meal_periods_dict.keys():
        print("\n################################\n")
        body_msg += "\n################################\n\n"
        url = 'https://api.dineoncampus.com/v1/location/61f9d7c8a9f13a15d7c1a25e/periods/' + meal_periods_dict[
            period] + '?platform=0&date=' + date
        period_response = requests.get(url)
        json_data = json.loads(period_response.text)

        data = json_data['menu']['periods']

        print("Meal Period:", data['name'], '\n')
        body_msg += "Meal Period:" + data['name'] + '\n\n'

        for category in data['categories']:
            print(category['name'])
            body_msg += category["name"] + "\n"
            for item in category['items']:
                print("\t", item['name'])
                body_msg += "\t" + item["name"] + "\n"

                if data["name"] not in list_mealperiod and category["name"] not in list_category:
                    tabular_table.add_row([data["name"], category["name"].title(), item["name"]])
                    list_mealperiod.append(data["name"])
                    list_category.append(category["name"])
                elif data["name"] in list_mealperiod and category["name"] not in list_category:
                    tabular_table.add_row(["", category["name"].title(), item["name"]])
                    list_category.append(category["name"])
                elif data["name"] in list_mealperiod and category["name"] in list_category:
                    tabular_table.add_row(["", "", item["name"]])
        list_category = []

    alt = tabular_table.get_html_string().replace("table","tbody")

    html = html.replace("REPLACE-HERE", alt)

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    # subject = "Today's Menu: " + date

    # msg = f"Subject: {subject} \n\n {body_msg}"
    msg.attach(part1)
    msg.attach(part2)

    # for i in range(len(customer_list)):  # property of theo lostoski
    #     stmp.sendmail(truegrit_user, customer_list[i], msg)

    stmp.sendmail(truegrit_user, customer_list[0], msg.as_string())
    print("END")