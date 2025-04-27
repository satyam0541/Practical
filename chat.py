# E-Commerce Chatbot with Option Usage Limits
def chatbot():
    print("Welcome to our E-Commerce Chatbot! ")

    # Dictionary structure for menu
    menu = {
        "1": {
            "title": "Track Order ",
            "options": {
                "1": "Check Order Status",
                "2": "Cancel an Order",
                "3": "Return or Replace",
            },
            "data": {
                "1": "Your order #12345 is currently out for delivery. Expected delivery: Tomorrow.",
                "2": "To cancel your order, visit: https://www.example.com/cancel-order",
                "3": "Return or replace your product by following this link: https://www.example.com/return-order",
            }
        },
        "2": {
            "title": "Products ",
            "options": {
                "1": "Electronics",
                "2": "Fashion",
                "3": "Home & Kitchen",
            },
            "data": {
                "1": "You can buy at https://www.example.com/Electronics",
                "2": "You can buy at https://www.example.com/Fashion",
                "3": "You can buy at https://www.example.com/Essentials",
            }
        },
        "3": {
            "title": "Customer Support ",
            "options": {
                "1": "Chat with Support",
                "2": "FAQs",
                "3": "Report an Issue",
            },
            "data": {
                "1": "Chat with a support agent here: https://www.example.com/chat-support",
                "2": "Read FAQs: How to track orders, return policy, and more. https://www.example.com/faqs",
                "3": "Report an issue with your order or product: https://www.example.com/report-issue",
            }
        },
        "4": {
            "title": "Deals & Offers ",
            "options": {
                "1": "Today's Deals",
                "2": "Coupons & Discounts",
                "3": "Membership Offers",
            },
            "data": {
                "1": "Today's Deals:\n- iPhone 14 (20% off) - $799\n- Adidas Sneakers (Buy 1 Get 1 Free)\n- 50% off on Kitchen Appliances",
                "2": "Active Coupons:\n- SAVE10 - 10% off on all orders\n- FREESHIP - Free shipping on orders above $50.",
                "3": "Membership Offers:\n- Prime Members: Extra 5% cashback\n- Free delivery for VIP customers",
            }
        }
    }

    usage_limit = 2

    usage_tracker = {}

    while True:
        # print("\nPlease select an option:")
        for key, value in menu.items():
            print(f"{key}. {value['title']}")
        print("5. Exit ")

        main_choice = input("\nEnter the number of your choice: ")
        print()

        if main_choice in menu:

            for sub_key, sub_value in menu[main_choice]["options"].items():
                print(f"{sub_key}. {sub_value}")

            sub_choice = input("\nEnter the number of your sub-choice: ")

            if sub_choice in menu[main_choice]["options"]:
                # Track option usage
                key_pair = f"{main_choice}-{sub_choice}"
                usage_tracker[key_pair] = usage_tracker.get(key_pair, 0) + 1

                # Check if usage limit is exceeded
                if usage_tracker[key_pair] > usage_limit:
                    print("\nYou have reached the maximum usage limit for this option.")
                print(menu[main_choice]["data"][sub_choice])
                print()
            else:
                print("\nInvalid sub-choice. Returning to main menu.")

        elif main_choice == "5":
            print("\nThank you for using our chatbot!")
            break
        else:
            print("\n Invalid choice. Please try again.")

chatbot()
