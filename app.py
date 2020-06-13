from flask import Flask, render_template, request
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#initialization
app = Flask(__name__)

#defining route of page
@app.route("/")
def layout():
    return render_template("stats.html", death="N/A", active="N/A", discharge="N/A", date="N/A", country="Not Selected", totalc="N/A", death2="N/A", active2="N/A", discharge2="N/A", country2="Not Selected", totalc2="N/A")


@app.route("/stats", methods=["POST"])
def stats():
    country2 = request.form.get("country2")
    country1 = request.form.get("country1")
    if not country1:
        return "Error, Enter a country for country 1..."
    if country1 == country2:
        return "Can't Select the same countries for Comparision"
    if country1 == "usa":

        covid_url= 'https://news.google.com/covid19/map?hl=en-IN&mid=/m/09c7w0&gl=IN&ceid=IN:en'

        uClient = uReq(covid_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #Scraping

        #total Cases:
        container = page_soup.findAll("div",{"class":"fNm5wd qs41qe"})
        container_html = container[0]
        active_c = container_html.findAll("div",{"class":"UvMayb"})
        totalc_str = active_c[0].text
        totalc = totalc_str.replace(',','')
        totalcx = int(totalc)
        #recovered
        r_container = page_soup.findAll("div",{"class":"fNm5wd gZvxhb"})
        r_container_html = r_container[0]
        recovered_c = r_container_html.findAll("div",{"class":"UvMayb"})
        recovered_str = recovered_c[0].text
        recovered = recovered_str.replace(',','')

        d_container = page_soup.findAll("div",{"class":"fNm5wd ckqIZ"})
        d_container_html = d_container[0]
        death_c = d_container_html.findAll("div",{"class":"UvMayb"})
        death_str = death_c[0].text
        death = death_str.replace(',','')

        active = "N/A"

        countryname = "USA"
    elif country1 == "india":


            ##########---Scraping (india)---##########

            #storing the url of website into var
            covid_url = 'https://www.mygov.in/covid-19'

            #Grabbing the html page from url and storing it in var "page_html"
            uClient = uReq(covid_url)
            page_html = uClient.read()
            uClient.close()

            #html parsing
            page_soup = soup(page_html, "html.parser")

            #death info
            dcontainers = page_soup.findAll("div",{"class":"iblock death_case"})
            deathcontainer = dcontainers[0]
            deathcount_container = deathcontainer.findAll("span",{"class":"icount"})
            death = deathcount_container[0].text

            #active Cases
            container = page_soup.findAll("div",{"class":"iblock active-case"})
            container_html = container[0]
            active_c = container_html.findAll("span",{"class":"icount"})
            active = active_c[0].text

            #recovered Cases
            r_container = page_soup.findAll("div",{"class":"iblock discharge"})
            r_container_html = r_container[0]
            recovered_c = r_container_html.findAll("span",{"class":"icount"})
            recovered = recovered_c[0].text
            ##########------##########

            #calc total cases
            totalcx = int(recovered)+int(active)+int(death)
            totalc = str(totalcx) + "~"

            countryname = "India"
    if not country2:
        return "Error, Enter a country for country 2..."
    if country2 == "usa":

        covid_url= 'https://news.google.com/covid19/map?hl=en-IN&mid=/m/09c7w0&gl=IN&ceid=IN:en'

        uClient = uReq(covid_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #Scraping

        #total Cases:
        container = page_soup.findAll("div",{"class":"fNm5wd qs41qe"})
        container_html = container[0]
        active_c = container_html.findAll("div",{"class":"UvMayb"})
        totalc_str = active_c[0].text
        totalc2 = totalc_str.replace(',','')
        totalc2s = totalc2
        #recovered
        r_container = page_soup.findAll("div",{"class":"fNm5wd gZvxhb"})
        r_container_html = r_container[0]
        recovered_c = r_container_html.findAll("div",{"class":"UvMayb"})
        recovered_str = recovered_c[0].text
        recovered2 = recovered_str.replace(',','')

        d_container = page_soup.findAll("div",{"class":"fNm5wd ckqIZ"})
        d_container_html = d_container[0]
        death_c = d_container_html.findAll("div",{"class":"UvMayb"})
        death_str = death_c[0].text
        death2 = death_str.replace(',','')

        active2 = "N/A"

        country2name = "USA"
    elif country2 == "india":


            ##########---Scraping (india)---##########

            #storing the url of website into var
            covid_url = 'https://www.mygov.in/covid-19'

            #Grabbing the html page from url and storing it in var "page_html"
            uClient = uReq(covid_url)
            page_html = uClient.read()
            uClient.close()

            #html parsing
            page_soup = soup(page_html, "html.parser")

            #death info
            dcontainers = page_soup.findAll("div",{"class":"iblock death_case"})
            deathcontainer = dcontainers[0]
            deathcount_container = deathcontainer.findAll("span",{"class":"icount"})
            death2 = deathcount_container[0].text

            #active Cases
            container = page_soup.findAll("div",{"class":"iblock active-case"})
            container_html = container[0]
            active_c = container_html.findAll("span",{"class":"icount"})
            active2 = active_c[0].text

            #recovered Cases
            r_container = page_soup.findAll("div",{"class":"iblock discharge"})
            r_container_html = r_container[0]
            recovered_c = r_container_html.findAll("span",{"class":"icount"})
            recovered2 = recovered_c[0].text
            ##########------##########

            #calc total cases
            totalc2s = int(recovered2)+int(active2)+int(death2)
            totalc2 = str(totalc2s) + "~"

            country2name = "India"


    #########################Calculations for Comparision###########################

    ########Deaths###########

    if death == "N/A" or death2 == "N/A":
        comp_death_country = "N/A"
        comp_death_count = "N/A"
    elif death>death2:
        comp_death_country = country2name
        comp_death_count = int(death2) - int(death)
    elif death2>death:
        comp_death_country = countryname
        comp_death_count = int(death) - int(death2)

    ######Active###########

    if active == "N/A" or active2 == "N/A":
        comp_active_country = "N/A"
        comp_active_count = "N/A"
    elif active<active2:
        comp_active_country = countryname
        comp_active_count = int(active) - int(active2)
    elif active2<active:
        comp_active_country = country2name
        comp_active_count = int(active2) - int(active)

    ##########Recovered Percentage###########

    if recovered == "N/A" or recovered2 == "N/A":
        comp_rec_country = "N/A"
        comp_rec_count = "N/A"
    elif recovered<recovered2:
        comp_rec_country = countryname
        comp_rec_count = (int(recovered) / int(totalcx))*100
    elif recovered2<recovered:
        comp_rec_country = country2name
        comp_rec_count = (int(recovered2)/int(totalc2s))*100

    #########Total Cases######################

    if int(totalcx) < int(totalc2s):
        comp_total_country = country2name
        comp_total_count = int(totalc2s) - int(totalcx)
    if int(totalc2s) < int(totalcx):
        comp_total_country = countryname
        comp_total_count = int(totalcx) - int(totalc2s)

    #################################################################################

    #############Clacs (other)##########

    comp_rec_count = round(comp_rec_count, 2)

    #####Misc##########

    if comp_death_count>0:
        sign="+"
    else:
        sign="-"

    if comp_total_count>0:
        sign2="+"
    else:
        sign2="-"

    return render_template("stats.html", death=death, active=active, discharge=recovered, totalc=totalc, country=countryname, country2=country2name,  death2=death2, active2=active2, discharge2=recovered2, totalc2=totalc2, dcompcountry=comp_death_country, dcompcount=comp_death_count, acompcount=comp_active_count, acompcountry=comp_active_country, reccountry=comp_rec_country, reccount=comp_rec_count, sign=sign, totalcompcountry=comp_total_country, totalcompcount=comp_total_count, sign2=sign2)

#running webapp
if (__name__) == "__main__":
    app.run()
