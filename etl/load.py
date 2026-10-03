
from etl.database import get_connection


def load_data(df):

    connection = get_connection()
    cursor = connection.cursor()

    # Clear the existing clean table before loading fresh transformed data
    cursor.execute("TRUNCATE TABLE qatarret_clean")

    query = """
        INSERT INTO qatarret_clean (
            `Order ID`,
            `Order Date`,
            `Customer ID`,
            `City`,
            `Salesperson`,
            `Product`,
            `Category`,
            `Quantity`,
            `Unit Price`,
            `Discount`,
            `Sales Channel`,
            `Payment Method`,
            `Customer Type`,
            `Revenue`,
            `Cost`,
            `Profit`
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s
        )
    """

    data = [
        tuple(row)
        for row in df[
            [
                "Order ID",
                "Order Date",
                "Customer ID",
                "City",
                "Salesperson",
                "Product",
                "Category",
                "Quantity",
                "Unit Price",
                "Discount",
                "Sales Channel",
                "Payment Method",
                "Customer Type",
                "Revenue",
                "Cost",
                "Profit"
            ]
        ].itertuples(index=False, name=None)
    ]

    cursor.executemany(query, data)

    connection.commit()

    print("Load successful!")
    print("Rows loaded:", cursor.rowcount)

    cursor.close()
    connection.close()

