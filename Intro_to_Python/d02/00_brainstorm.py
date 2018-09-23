# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_brainstrom.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zewang <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 10:31:49 by zewang            #+#    #+#              #
#    Updated: 2018/07/12 13:40:54 by zewang           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def generate(n):
    return random.randint(1, n)
    

        
category1 = ['computer', 'people', 'learn', 'fortnite', 'sucks', 'pubg', 'better', 'mouse','china', 'hair'];
category2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
category3 = ["a","b","c","d","e","f","g","h","i","j"];


print(random.choice(category1))
