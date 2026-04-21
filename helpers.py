url = "https://practicesoftwaretesting.com/"
time_max = 15
time_wait = 15
time_mid = 2
time_min = 1

admin_email = "admin@practicesoftwaretesting.com"
admin_password = "welcome01"

"""EXPECTED"""
EXPECTED = {
    "nav-home": "Start",
    "nav-categories": "Kategorien",
    "nav-hand-tools": "Hand Werkzeuge",
    "nav-power-tools": "Elektrische Werkzeuge",
    "nav-other": "Andere",
    "nav-special-tools": "Spezial Werkzeuge",
    "nav-rentals": "Mietgeräte",
    "nav-contact": "Kontakt",
    "nav-sign-in": "Einloggen",
}

"""MAIN PAGE"""
top_menu_sign_in = "//a[text()='Sign in']"
top_menu_home = "//a[text()='Home']"
top_menu_contact = "//a[text()='Contact']"
top_menu_category = "//a[normalize-space()='Categories']"
top_menu_category_de = "//a[normalize-space()='Kategorien']"
top_menu_cart_shopping = "(//*[contains(@class, 'cart-shopping')])[1]"
top_menu_select_language = "//button[@id='language']"
btn_lang_de = "//a[@data-test='lang-de']"

subcategory_handing_tools = "//a[text()='Hand Tools']"

first_card_main_page = "(//a[@class='card'])[1]"

sort_select_main_page = "//select[@class='form-select']"

select_sort_main_page = "//option[text()='Price (High - Low)']"
slider_min_main_page = "//span[contains(@class, 'pointer-min') and @aria-valuetext='0']"
slider_max_main_page = (
    "//span[contains(@class, 'pointer-max') and @aria-valuetext='100']"
)
search_main_page = "//input[@id ='search-query']"
search_btn_main_page = "//button[text()='Search ']"
checkbox_category_main_page = "//input[@name='category_id' and @type='checkbox']"
checkbox_brand_main_page = "//input[@name='brand_id' and @type='checkbox']"

text_nav_home_main_page = "//a[@data-test='nav-home']"
text_nav_categories_main_page = "//a[@data-test='nav-categories']"
text_nav_categories_hand_tools_main_page = "//a[@data-test='nav-hand-tools']"
text_nav_categories_power_tools_main_page = "//a[@data-test='nav-power-tools']"
text_nav_categories_other_main_page = "//a[@data-test='nav-other']"
text_nav_categories_special_tools_main_page = "//a[@data-test='nav-special-tools']"
text_nav_categories_nav_rentals_main_page = "//a[@data-test='nav-rentals']"
text_nav_contact_main_page = "//a[@data-test='nav-contact']"
text_nav_sign_in_main_page = "//a[@data-test='nav-sign-in']"

"""LOGIN"""
login_title = "//h3[text()='Login']"
email_login_page = "//input[@type='email']"
password_login_page = "//input[@type='password']"
login_btn_login_page = "//input[@type='submit']"
btn_register_your_account = "//a[text()='Register your account']"


"""REGISTRATION PAGE"""
customer_registration_title = "//h3[text()='Customer registration']"

"""REGISTRATION PAGE"""
btn_register_reg_page = "//button[text()='Register ']"

first_name_reg_page = "//label[text()='First name']/../input"
last_name_reg_page = "//label[text()='Last name']/../input"
birth_date_reg_page = "//label[text()='Date of Birth *']/../input"
street_reg_page = "//label[text()='Street']/../input"
postal_code_reg_page = "//label[text()='Postal code']/../input"
city_reg_page = "//label[text()='City']/../input"
state_reg_page = "//label[text()='State']/../input"
country_reg_page = "//option[text()='Your country *']"
phone_reg_page = "//label[text()='Phone']/../input"
email_reg_page = "//label[text()='Email address']/../input"
password_reg_page = "//label[text()='Password']/..//input"

dropdown_list_country_reg_page = "//option[text()='United States of America (the)']"

register_btn_reg_page = "//button[text()='Register ']"

"""MY ACCOUNT PAGE"""
title_account_page = "//h1[text()='My account']"
profile_account_page = ".//a[@href='/account/profile' and @role='button']"

input_text_first_name_account_page_filled = "//input[@id='first_name']"
input_text_last_name_account_page_filled = "//input[@id='last_name']"
input_text_email_account_page_filled = "//input[@id='email']"
input_text_phone_account_page_filled = "//input[@id='phone']"
input_text_street_account_page_filled = "//input[@id='street']"
input_text_postal_code_account_page_filled = "//input[@id='postal_code']"
input_text_city_account_page_filled = "//input[@id='city']"
input_text_state_account_page_filled = "//input[@id='state']"
input_text_country_account_page_filled = "//input[@id='country']"

"""PRODUCT PAGE"""
count_field_product_page = "//label[text()='Quantity']/..//input[@type='number']"
btn_more_product_page = "(//button[@class = 'btn btn-secondary'])[2]"
add_to_cart_product_page = "//button[normalize-space()='Add to cart']"


"""CART PAGE"""
product_name_cart_page = "//span[@class='product-title']"

btn_proceed_to_checkout = (
    "//button[@data-test='proceed-1' and normalize-space()='Proceed to checkout']"
)
btn_proceed_to_checkout_2 = (
    "//button[@data-test='proceed-2' and normalize-space()='Proceed to checkout']"
)
btn_proceed_to_checkout_3 = (
    "//button[@data-test='proceed-3' and normalize-space()='Proceed to checkout']"
)

btn_confirm_cart_page = "//button[normalize-space()='Confirm']"

text_hello_admin_product_page = "//p[normalize-space()='Hello John Doe, you are already logged in. You can proceed to checkout.']"
input_field_street_cart_page = "//input[@id='street']"
input_field_city_cart_page = "//input[@id='city']"
input_field_state_cart_page = "//input[@id='state']"
input_field_country_cart_page = "//input[@id='country']"
input_field_postal_code_cart_page = "//input[@id='postal_code']"
payment_title_cart_page = "//h3[normalize-space()='Payment']"
select_payment_method = "//select[@id='payment-method']"
select_cash_to_delivery_cart_page = "//option[text()='Cash on Delivery']"
success_notification_cart_page = "//div[text()='Payment was successful']"

"""CONTACT PAGE"""
btn_attachment_contact_page = "//label[text()='Attachment']"
btn_send_message_contact_page = "//input[@class='btnSubmit']"

contact_title = "//h3[text()='Contact']"

input_field_first_name_contact_page = "//input[@id='first_name']"
input_field_last_name_contact_page = "//input[@id='last_name']"
input_field_email_contact_page = "//input[@id='email']"
select_subject_contact_page = "//select[@id='subject']"
input_field_message_contact_page = "//textarea[@id='message']"

select_webmaster_contact_page = "//option[text()='Webmaster']"

test_file = r"C:\Users\Admin\PycharmProjects\project-name\PracticeSoftwareTesting\files\test.txt"

success_notification = (
    "//div[normalize-space()='Thanks for your message! We will contact you shortly.']"
)
