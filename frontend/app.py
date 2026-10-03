from etl.pipeline import run_pipeline
from etl.database import get_connection
import streamlit as st

st.set_page_config(
    page_title="Qatar Retail Data Entry",
    page_icon="🛒"
)

st.title("Qatar Retail — Data Entry")

st.write("Enter a new sales transaction.")

order_id = st.text_input("Order ID")

order_date = st.date_input("Order Date")

customer_id = st.text_input("Customer ID")

city = st.selectbox(
    "City",
    ["Doha", "Lusail", "Al Rayyan"]
)

salesperson = st.text_input("Salesperson")

product = st.text_input("Product")

category = st.selectbox(
    "Category",
    [
        "Electronics",
        "Furniture",
        "Office Equipment",
        "Networking"
    ]
)

quantity = st.number_input(
    "Quantity",
    min_value=1,
    step=1
)

unit_price = st.number_input(
    "Unit Price",
    min_value=0.0,
    step=0.01
)

discount = st.number_input(
    "Discount",
    min_value=0.0,
    max_value=1.0,
    step=0.01
)

sales_channel = st.selectbox(
    "Sales Channel",
    ["Retail", "online", "Corporate"]
)

payment_method = st.selectbox(
    "Payment Method",
    ["Card", "Cash", "Bank Transfer", "Credit"]
)

customer_type = st.selectbox(
    "Customer Type",
    ["Individual", "SME", "Enterprise"]
)

cost = st.number_input(
    "Cost",
    min_value=0.0,
    step=0.01
)


if st.button("Submit Transaction"):
    

    revenue = quantity * unit_price * (1 - discount)
    profit = revenue - cost

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO qatarret
        (`Order ID`, `Order Date`, `Customer ID`, `City`, `Salesperson`,
         `Product`, `Category`, `Quantity`, `Unit Price`, `Discount`,
         `Sales Channel`, `Payment Method`, `Customer Type`,
         `Revenue`, `Cost`, `Profit`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s)
    """

    
    values = (
        order_id,
        order_date,
        customer_id,
        city,
        salesperson,
        product,
        category,
        quantity,
        unit_price,
        discount,
        sales_channel,
        payment_method,
        customer_type,
        revenue,
        cost,
        profit
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    st.success("Transaction captured and saved to MySQL!")

    st.write("Revenue:", round(revenue, 2))
    st.write("Profit:", round(profit, 2))