#! /usr/local/bin/python3
import os
import sys
import socket

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # this is check ipv4
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # test for IP v4
        return False

    return True

def is_valid_ipv6_address(address):
    valid_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f', ':', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #address = input('Please enter an IP address: ')
    is_valid = []

    for i in range(len(address)):
       current = address[i]
       for j in range(len(valid_characters)):
          check = valid_characters[j]
          if check == current:
            a = 1
            is_valid.append(a)

    address_list = address.split(":")
    invalid_segment = False

    for i in range(len(address_list)):
      current = address_list[i]
      if len(current) > 4:
        invalid_segment = True

    if len(address) == len(is_valid) and len(address_list) == 8 and invalid_segment == False:
       print (address)
       print("It is a valid IPv6 address.")

    elif invalid_segment:
       print (address)
       print("It is not a valid IPv6 address.")

    else:
       print("It is not a valid IPv6 address.")


with open("./input_file.txt") as f:
    for line1 in f:
        #print (line)
        #addr="'"+line+"'"
        #print (addr) 
        line=line1.rstrip()  
        a_ipv4=is_valid_ipv4_address(line)
        #a_ipv6=is_valid_ipv6_address(line)
        if a_ipv4: 
          print (line+" is ipv4")
        else:
          #print (line+" is ipv6")
          is_valid_ipv6_address(line)
