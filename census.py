#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 08:28:22 2020

@author: u7075106
"""
canberra_population = 196037
canberra_families = 50352
couples_children = 22850
single_parent_children = 7243
avg_children = 1.8
families_with_children = couples_children + single_parent_children
couples_without_children = canberra_families - families_with_children
number_of_children = families_with_children * avg_children
number_of_adults = canberra_population - number_of_children
number_of_single_adult = number_of_adults - couples_children - couples_without_children
print(number_of_adults)



