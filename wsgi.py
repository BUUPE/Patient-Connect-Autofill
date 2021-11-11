# Created by Phil Ledoit

from flask import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

app = Flask(__name__, template_folder='templates')

driver = 0
times = []
bu_username, bu_password = "sample", "sample"


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/home/", methods=['GET', 'POST'])
def home():
    global bu_username, bu_password
    if request.method == 'POST':
        bu_username = request.form['username']
        bu_password = request.form['password']
    else:
        bu_username = request.form['username']
        bu_password = request.form['password']
    return render_template('home.html', status_message="")


@app.route("/survey/")
def survey():
    load_chrome_driver()
    complete_survey()
    driver.close()
    return render_template('index.html', status_message="Survey complete")


@app.route("/appointment/")
def appointment():
    load_chrome_driver()
    appointment_checklist()
    return render_template('appt_location.html', status_message="Appointment pending")


@app.route("/both/")
def both():
    load_chrome_driver()
    complete_survey()
    appointment_checklist()
    return render_template('appt_location.html', status_message="Survey complete")


@app.route("/loc0/")
def loc0():
    appointment_location(0)
    return render_template('appt_time.html', status_message="808 Commonwealth Ave.", t0=times[0], t1=times[1],
                           t2=times[2],
                           t3=times[3], t4=times[4], t5=times[5], t6=times[6], t7=times[7], t8=times[8], t9=times[9])


@app.route("/loc1/")
def loc1():
    appointment_location(1)
    return render_template('appt_time.html', status_message="72 Concord St.", t0=times[0], t1=times[1],
                           t2=times[2],
                           t3=times[3], t4=times[4], t5=times[5], t6=times[6], t7=times[7], t8=times[8], t9=times[9])


@app.route("/time0/")
def time0():
    appointment_time(0)
    driver.close()
    return render_template('index.html', status_message="Appointment booked")


@app.route("/time1/")
def time1():
    appointment_time(1)
    driver.close()
    return render_template('index.html', status_message="Appointment booked")


@app.route("/time2/")
def time2():
    appointment_time(2)
    driver.close()
    return render_template('index.html', status_message="Appointment booked")


@app.route("/time3/")
def time3():
    appointment_time(3)
    driver.close()
    return render_template('index.html', status_message="Appointment booked")


@app.route("/time4/")
def time4():
    appointment_time(4)
    driver.close()
    return render_template('index.html', status_message="Appointment booked")


@app.route("/time5/")
def time5():
    appointment_time(5)
    driver.close()
    return render_template('index.html', status_message="Appointment booked")


@app.route("/time6/")
def time6():
    appointment_time(6)
    driver.close()
    return render_template('index.html', status_message="Appointment booked")


@app.route("/time7/")
def time7():
    appointment_time(7)
    driver.close()
    return render_template('index.html', status_message="Appointment booked")


@app.route("/time8/")
def time8():
    appointment_time(8)
    driver.close()
    return render_template('index.html', status_message="Appointment booked")


@app.route("/time9/")
def time9():
    appointment_time(9)
    driver.close()
    return render_template('index.html', status_message="Appointment booked")


# to set up the Chrome webdriver
def load_chrome_driver():
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument("--disable-extensions")
    user_agent = 'Chrome/60.0.3112.50'
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return 0


# to log into Patient Connect
def log_into_patient_connect(f_username, f_password):
    user_field = driver.find_element(By.ID, 'j_username')
    user_field.send_keys(f_username)

    user_field = driver.find_element(By.ID, 'j_password')
    user_field.send_keys(f_password)

    login_continue = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/form/button')
    login_continue.click()

    return 0


# to complete the survey
def complete_survey():
    if driver.current_url != 'https://patientconnect.bu.edu/home.aspx':
        driver.get('https://patientconnect.bu.edu/home.aspx')

    if driver.current_url != 'https://patientconnect.bu.edu/home.aspx':
        log_into_patient_connect(bu_username, bu_password)

    driver.get('https://patientconnect.bu.edu/Mvc/Patients/QuarantineSurvey')

    driver.get('https://patientconnect.bu.edu/CheckIn/Survey/ShowAll/21')

    question_1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/form/div[2]/fieldset/div/div[1]/div')
    question_1.click()

    continue_2 = driver.find_element(By.XPATH, '//*[@id="mainbody"]/footer/div/div[2]/input')
    continue_2.click()

    return 0


# to start booking an appointment
def appointment_checklist():
    if driver.current_url != 'https://patientconnect.bu.edu/home.aspx':
        driver.get('https://patientconnect.bu.edu/home.aspx')

    if driver.current_url != 'https://patientconnect.bu.edu/home.aspx':
        log_into_patient_connect(bu_username, bu_password)

    driver.get('https://patientconnect.bu.edu/appointments_home.aspx')

    schedule_appointment = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/form/p[1]/input')
    schedule_appointment.click()

    not_911 = driver.find_element(By.XPATH,
                                  '/html/body/div[4]/div/div[2]/form/span/fieldset/table/tbody/tr[1]/td/span/label')
    not_911.click()

    continue_3 = driver.find_element(By.XPATH, '//*[@id="cmdProceed"]')
    continue_3.click()

    reason = driver.find_element(By.XPATH, '//*[@id="ctl03"]/fieldset/table/tbody/tr[13]/td/span')
    reason.click()

    continue_4 = driver.find_element(By.XPATH, '//*[@id="cmdProceed"]')
    continue_4.click()

    agree1 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/form/fieldset/table/tbody/tr[1]/td/span/input')
    agree1.click()

    continue_5 = driver.find_element(By.XPATH, '//*[@id="cmdProceed"]')
    continue_5.click()

    agree2 = driver.find_element(By.XPATH,
                                 '/html/body/div[4]/div/div[2]/form/span/li[4]/fieldset/table/tbody/tr[1]/td/span/label')
    agree2.click()

    continue_6 = driver.find_element(By.XPATH, '//*[@id="cmdProceed"]')
    continue_6.click()

    no_symptoms = driver.find_element(By.XPATH,
                                      '/html/body/div[4]/div/div[2]/form/fieldset/table/tbody/tr[3]/td/span/label')
    no_symptoms.click()

    continue_7 = driver.find_element(By.XPATH, '//*[@id="cmdProceed"]')
    continue_7.click()

    not_positive = driver.find_element(By.XPATH,
                                       '/html/body/div[4]/div/div[2]/form/fieldset/table/tbody/tr[3]/td/span/label')
    not_positive.click()

    continue_8 = driver.find_element(By.XPATH, '//*[@id="cmdProceed"]')
    continue_8.click()

    continue_9 = driver.find_element(By.XPATH, '//*[@id="cmdStandardProceed"]')
    continue_9.click()

    return 0


# to select the location of the appointment
def appointment_location(location_choice):
    testing_location = Select(driver.find_element(By.ID, "LocationList"))
    testing_location.select_by_index(location_choice + 1)

    search_appointments = driver.find_element(By.XPATH, '//*[@id="apptSearch"]')
    search_appointments.click()

    for counter in range(1, 11):
        appointment_results_xpath = '/html/body/div[4]/div/div[2]/form/div[2]/fieldset/table/tbody/tr[' \
                                    + str(counter) + ']/td[2]/label'
        times.append(driver.find_element(By.XPATH, appointment_results_xpath).text)

    return 0


# to choose the date and time of the appointment
def appointment_time(time_choice):
    appointment_xpath = "//*[@id='apptContainer']/fieldset/table/tbody/tr[" + str(
        time_choice + 1) + "]/td[2]/label"
    select_appointment = driver.find_element(By.XPATH, appointment_xpath)
    select_appointment.click()

    continue_10 = driver.find_element(By.ID, "cmdStandardProceedUpper")
    continue_10.click()

    confirm_appointment = driver.find_element(By.XPATH, '//*[@id="cmdConfirm"]')
    confirm_appointment.click()

    return 0


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
