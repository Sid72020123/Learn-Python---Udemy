import os
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()

# Keep the browser open
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

ACCOUNT_EMAIL = "sid@test.com"
ACCOUNT_PASSWORD = "superSecretTestPassword"
GYM_URL = "https://appbrewery.github.io/gym/"

# Create a new driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

email_entry = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
password_entry = driver.find_element(By.ID, "password-input")
login_submit_button = driver.find_element(By.ID, "submit-button")

email_entry.clear()
email_entry.send_keys(ACCOUNT_EMAIL)
password_entry.clear()
password_entry.send_keys(ACCOUNT_PASSWORD)
login_submit_button.click()

wait.until(
    EC.presence_of_element_located((By.ID, "schedule-page"))
)  # Wait until successful login


def get_class_schedules():
    raw_schedules = driver.find_elements(By.CLASS_NAME, "Schedule_dayGroup__y79__")
    details = {}
    for schedule in raw_schedules:
        schedule_day = schedule.find_element(By.TAG_NAME, "h2").text
        if "(" in schedule_day:
            schedule_date = (
                schedule_day.split("(")[1].split(",")[1].replace(")", "").strip()
            )
            schedule_day = schedule_day.split("(")[1].split(",")[0]
        else:
            schedule_date = schedule_day.split(",")[1].strip()
            schedule_day = schedule_day.split(",")[0]
        details[schedule_day] = []

        gym_classes = schedule.find_elements(By.CLASS_NAME, "ClassCard_card__KpCx5")

        for gym_class in gym_classes:
            class_name = (
                gym_class.find_element(By.TAG_NAME, "h3")
                .text.replace("Class", "")
                .strip()
            )
            class_details = gym_class.find_elements(
                By.CLASS_NAME, "ClassCard_classDetail__Z8Z8f"
            )
            class_time = str(class_details[0].text.replace("Time:", "")).strip()
            class_instructor = str(
                class_details[1].text.replace("Instructor:", "")
            ).strip()
            class_duration = str(class_details[2].text.replace("Duration:", "")).strip()
            seats_available = (
                class_details[3]
                .text.replace("Available:", "")
                .replace(" spots", "")
                .replace(" ", "")
                .split("/")
            )

            card_actions = gym_class.find_element(
                By.CLASS_NAME, "ClassCard_cardActions__tVZBm"
            )
            button_id = card_actions.find_element(By.TAG_NAME, "button").get_attribute(
                "id"
            )

            class_dict = {
                "name": class_name,
                "date": schedule_date,
                "time": class_time,
                "instructor": class_instructor,
                "duration": class_duration,
                "seats_available": [int(i) for i in seats_available],
                "button_id": button_id,
            }
            details[schedule_day].append(class_dict)
    return details


def get_bookings_list():
    confirmed_bookings_section = driver.find_element(
        By.ID, "confirmed-bookings-section"
    )
    waitlist_section = driver.find_element(By.ID, "waitlist-section")

    bookings_info = confirmed_bookings_section.find_elements(
        By.CLASS_NAME, "MyBookings_bookingCard__VRdrR"
    )

    waitlists_info = waitlist_section.find_elements(
        By.CLASS_NAME, "MyBookings_waitlist__rD_tl"
    )

    combined_bookings_info = list(bookings_info + waitlists_info)

    BOOKINGS = []

    for each_booking in combined_bookings_info:
        class_type = "booked"
        class_name = (
            each_booking.find_element(By.TAG_NAME, "h3")
            .text.replace("Class", "")
            .strip()
        )
        if "(Waitlist)" in class_name:
            class_type = "waitlisted"
            class_name = class_name.replace("(Waitlist)", "").strip()
        class_details = each_booking.find_elements(By.TAG_NAME, "p")
        class_time = class_details[0].text.replace("When:", "")
        class_day = class_time.split(",")[0].strip()
        class_date = class_time.split(",")[1].strip()
        class_time = class_time.split(",")[2].strip()
        class_instructor = str(class_details[1].text.replace("Instructor:", "")).strip()
        class_duration = (
            str(class_details[2].text.replace("Duration:", "")).strip()
            if class_type == "booked"
            else None
        )
        BOOKINGS.append(
            {
                "type": class_type,
                "name": class_name,
                "day": class_day,
                "date": class_date,
                "time": class_time,
                "instructor": class_instructor,
                "duration": class_duration,
            }
        )
    return BOOKINGS


CLASS_SCHEDULES = get_class_schedules()

# pprint(get_class_schedules())

BOOKING_TYPES = {
    "Booked": {
        "text": "already booked",
        "count": 0,
        "summary_text": "already booked classes",
        "detailed_summary_text": "Already Booked",
    },
    "Waitlisted": {
        "text": "already on waitlist",
        "count": 0,
        "summary_text": "already joined waitlists",
        "detailed_summary_text": "Already on Waitlist",
    },
    "Join Waitlist": {
        "text": "joined waitlist",
        "count": 0,
        "summary_text": "waitlists joined",
        "detailed_summary_text": "New Waitlist",
    },
    "Book Class": {
        "text": "booked",
        "count": 0,
        "summary_text": "classes booked",
        "detailed_summary_text": "New Booking",
    },
}

BOOKING_LOGS = []

# print(CLASS_SCHEDULES)

for schedule in CLASS_SCHEDULES:
    if schedule in ["Tue", "Wed", "Thu"]:
        for class_info in CLASS_SCHEDULES[schedule]:
            if class_info["time"] == "6:00 PM":
                button = driver.find_element(By.ID, class_info["button_id"])
                button_text = button.text.strip()
                button.click()

                BOOKING_TYPES[button_text]["count"] += 1
                booking_type_text = BOOKING_TYPES[button_text]["text"]
                booking_info_text = f"{class_info['name']} Class on {schedule}, {class_info['date']} {class_info['time']}"
                print(f"✓ {booking_type_text.capitalize()}: {booking_info_text}")

                BOOKING_LOGS.append(
                    {
                        "type": BOOKING_TYPES[button_text]["detailed_summary_text"],
                        "text": booking_info_text,
                    }
                )

print("\n=== *** BOOKING SUMMARY *** ===")
for bt in BOOKING_TYPES.values():
    print(f"[*] {bt['summary_text'].title()}: {bt['count']}")

print("\n=== *** DETAILED CLASS LIST *** ===")
for bl in BOOKING_LOGS:
    print(f"\t* [{bl['type']}] {bl['text']}")

sleep(1)

driver.find_element(By.ID, "my-bookings-link").click()
wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))

print(get_bookings_list())
