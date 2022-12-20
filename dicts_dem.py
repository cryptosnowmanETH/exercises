#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_input(booking_data):
    for field, field_data in booking_data.items():
        if field_data['is_valid']:
            field_data['field_value'] = input(field_data['prompt'])

    return booking_data


def validate(booking_data):
    for field, field_data in booking_data.items():
        field_data['is_valid'] = True
    return booking_data


def main():
    booking_data = {
        'customer_name': {
            'field_value': None,
            'prompt': 'Enter a customer name: ',
            'is_valid': False,
        },
        'package_description': {
            'field_value': None,
            'prompt': 'Enter a description of the package : ',
            'is_valid': False,
        },
        'weight': {
            'field_value': None,
            'prompt': 'Enter the weight of the package : ',
            'is_valid': False,
        },
    }
    booking_data = get_input(booking_data)
    validated_booking_data = validate(booking_data)
    booking_data = get_input(validated_booking_data)
    print(validated_booking_data)


if __name__ == "__main__":
    main()
