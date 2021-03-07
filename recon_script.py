#! /usr/bin/python3

'''
Tools:
    1.amass ---> configuration file in: ~/.config/amass/config.ini
    2.subfinder ---> configuration file in: ~/.config/subfinder/config.yaml
    3.github-subdomains --> github-search/.tokens || or in the run directory??
    4.assetfinder
    5.sublist3r

Brute force tools:
    1.amass
    2.shuffldns
'''

import os
import sys
import time

domain = sys.argv[1]

os.makedirs(domain + '/subdomains')
os.chdir(domain + '/subdomains')


def subdomains():

    os.system('amass enum -d ' + domain + ' -o amass.txt -config ~/.config/amass/config.ini')
    os.system('amass enum -d ' + domain + ' -active -o amass_active.txt -config ~/.config/amass/config.ini')
    os.system('amass enum -d ' + domain + ' -passive -o amass_passive.txt -config ~/.config/amass/config.ini')

    os.system('subfinder -d ' + domain + ' -config ~/config/subfinder/config.yaml -o subfinder.txt')
    os.system('subfinder -dL subfinder.txt -recursive -o subfinder_1_rec.txt')
    os.system('subfinder -dL subfinder_1_rec.txt -recursive -o subfinder_2_rec.txt')
    os.system('subfinder -dL subfinder_2_rec.txt -recursive -o subfinder_3_rec.txt')

    for i in range(5):
        os.system('github-subdomains -d ' + domain + ' > github_subdomains_' + str(i) + '.txt')  # there is configuration file in its directory. You only need to make it and store github tokens.
        time.sleep(6)
        if(i == 3):
            time.sleep(4)

    os.system('assetfinder --subs-only ' + domain + ' -o assetfinder.txt')
    os.system('sublist3r -d ' + domain + ' -v -o sublist3r.txt')


def bruteforcing():

    os.system('amass enum -brute -d ' + domain + ' -o amass_brute.txt')
    os.system('amass enum -brute -d ' + domain + ' -rf resolvers.txt -w sub_worlist.txt -o amass_brute_list.txt')

    os.system('shuffuledns -d ' + domain + ' -w sub_worlist.txt -r resolvers.txt -o shuffledns_brute.txt')


def collect_subdomains():

    # subdomains
    os.system('cat amass.txt > all.txt')
    os.system('cat amass_active.txt >> all.txt')
    os.system('cat amass_passive.txt >> all.txt')

    os.system('cat subfinder.txt >> all.txt')
    os.system('cat subfinder_1_rec.txt >> all.txt')
    os.system('cat subfinder_2_rec.txt >> all.txt')
    os.system('cat subfinder_3_rec.txt >> all.txt')

    for i in range(5):
        os.system('cat github_subdomains_' + str(i) + '.txt >> all.txt')

    os.system('cat assetfinder.txt >> all.txt')
    os.system('cat sublist3r.txt >> all.txt')

    # bruteforce
    os.system('cat amass_brute.txt >> all.txt')
    os.system('cat amass_brute_list.txt >> all.txt')

    os.system('cat shuffledns_brute.txt >> all.txt')

    # final all.txt
    os.system('cat all.txt | sort -u > final_subdomains.txt')


def live_subdomians():
    os.system("cat final_subdomains | httprobe -c 50 -t 3000 | sed 's/\\http\\:\\/\\///g' |  sed 's/\\https\\:\\/\\///g' | sort -u > live_subdomians.txt")


def port_scanning():
    os.system("echo 'PORT STATE  SERVICE VERSION  subdomain' > port_scanning.txt")
    for lines in range
        os.system("nmap -sV -T3 -Pn -p3868,3366,8443,8080,9443,9091,3000,8000,5900,8081,6000,10000,8181,3306,5000,4000,8888,5432,15672,9999,161,4044,7077,4040,9000,8089,443,7447,7080,8880,8983,5673,7443,19000,19080 " + $domain + " | grep -E 'open|filtered|closed'")


# def resolve_subdomains():
#     os.system('shuffledns -d ' + domain + ' -list final_subdomains.txt -o live.txt -r resolvers.txt')


subdomains()
bruteforcing()
collect_subdomains()
