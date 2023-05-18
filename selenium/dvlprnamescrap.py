from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import pandas as pd

# driver = webdriver.Chrome()
# url = ("https://apps.shopline.com/detail/?appHandle=zhekouhuodongsheji")
# driver.get(url)
# title = driver.find_elements(By.XPATH, ".//p[@class='body_4 color_grey1']")
# # print(title)
# # Convert the elements to text format
# title_texts = [title.text for title in title]
# # Print the converted text
# print(title_texts[0])

# driver.close


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

'''
#------------------------------------------------------------- App name Fetch -------------------------------------------------------------

# appurlls = []
# appls = []
# dvlprurl = []
# for i in range(1,8):
#     s = str(i)
#     url = (f"https://apps.shopline.com/sort/?pricing=all&type=0&appName=&strategy=appPopular&currentPage={s}")
#     # print(url)   
#     appurlls.append(url)
    
# # print(ls)
# for i in appurlls:
#     # print(i)
    
#     driver = webdriver.Chrome()
#     driver.get(i)
#     title = driver.find_elements(By.XPATH, ".//*[@class='title_3 color_black1 _appName_warp_1wuz5_34']")
#     # print(title)
#     # Convert the elements to text format
#     title_texts = [title.text for title in title]
#     # Print the converted text
#     for text in title_texts:
#         print(text)
#         appls.append(text)
#     driver.close
# print(appls)

'''
#------------------------------------------------------------- App name create urls -------------------------------------------------------------

# for i1 in appls:
#     dvurl = (f"https://apps.shopline.com/detail/?appHandle={i1}")
#     # print(url)   
#     dvlprurl.append(dvurl)

# # print(dvlprurl)
# for dvpurl in dvlprurl:
#     print(dvpurl)
    
#     driver = webdriver.Chrome()
#     driver.get(dvpurl)
#     developers = driver.find_elements(By.XPATH, ".//p[@class='body_4 color_grey1']")
#     # print(developers)
#     # Convert the elements to text format
#     developers_texts = [developers.text for developers in developers]
#     # Print the converted text
#     for dvlpr in developers_texts:
#         print(dvlpr)
#     driver.close



#------------------------------------------------------------- App name with uderscore -------------------------------------------------------------

import pandas as pd
import re

excel_file = "D:/wanbuffer/django/selenium/appname.xlsx" 
df = pd.read_excel(excel_file ,usecols='B')
data_list = df.values.tolist()
# print(data_list)

dvlprurl =[]

for row in data_list:
    # print(row[0])        
    app = re.sub(r"\s+", '_', row[0]).lower()
    # print(app)
    
    # create urls with app name
    dvurl = (f"https://apps.shopline.com/detail/?appHandle={app}")
    # print(dvurl)   
    dvlprurl.append(dvurl)
# print(dvlprurl)

# count= 1
# for i in dvlprurl:
#     print(count,i)
#     count+=1
'''# Get Developer name
try:
    driver = webdriver.Chrome()
    driver.get("https://apps.shopline.com/detail/?appHandle=design_maker_for_campaigns")
    developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
    # print(developers)
    # Convert the elements to text format
    developers_texts = [developers.text for developers in developers]
    developer = developers_texts[0] #developer name
    print(developer)
dvlls.append(developer)
    driver.close
except IndexError:
    print("web page not exits")
    
'''
dvlls =[]

try:
    count = 1
    for dvpurl in dvlprurl:
        # print(dvpurl)
        if dvpurl == "https://apps.shopline.com/detail/?appHandle=design_maker_for_campaigns":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=zhekouhuodongsheji"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=add_to_cart_button":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=add_to_cart"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=sales_popup":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=sales_notification"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=google_translate_helper":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=gugefanyizhushou"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=upsell_&_bundles":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=product_bundles"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=forms_&_popups":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=popups"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=page_speed_booster":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=xingnengyouhuabooster3451"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=cart_upsell_-_progress_bar":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=cart_upsell_progress_bar"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=payment_butler":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=fee_payment_butler"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=multi-platform_comment_collection":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=multi_platform_comment_collection"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=free_gift":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=gift_offer"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=variants_combination":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=variant_combination"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=easyrank_seo_all-in-one":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=seo_search_engine_optimization_2_0"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=product_filters_&_color_swatch":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=product_filters_color_palette"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=product_pin":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=product_boost_extension"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=instagram_feed":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=instagram-photo"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=salesmartly_chat":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=salesmartly"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=b2b_&_wholesale_solution":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=b2b_wholesale_solution"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=trustdecision_fraud_prevention":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=td_antifraud"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=smart_feed":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=smart_feed_prod"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=lucky_orange:_user_behavior_analysis":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=lucky_orange"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=shopify_store_one-click_migration":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=shopify_store_one_click_relocation"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=gdpr-privacy_banner":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=gdpr_yinsidanchuang"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=tiktok_marketing":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=tiktok-marketing"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=tiktok_for_business":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=tiktok-business-plugin"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=flow_automation":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=flow"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=multi-channel_pixel_installation":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=multiplatform_pixel_installation"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=stream_email&sms_marketing":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=stream_email_sms_marketing"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=3d_&_ar_product_viewer":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=product_3d_ar_display"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=pre-order":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=pre_order_now"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=installment_information_display":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=fenqixinxizhanshi"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=eprolo-dropshipping":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=eprolo_dropshipping"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=multi-language_translator":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=ugckeshihuafanyi"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=mademine:_easy_dropshipping":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=MadeMine"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=shoplazza_one-click_shop_migration_tool":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=shoplazza_one_click_shop_migration_tool"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=mambasms_sms&email_marketing":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=mambasms_sms_email_marketing"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=pingpong":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=pingpong1398"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=wotohub-_influencer_marketing_solution":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=wotohub_influencer_marketing_solution"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=picwish_-_ai_background_remover":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=picwish_ai_background_remover"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=buttonify-dropshipping_app":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=buttonify_dropshipping_app"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=poptin:_exit_intent,_pop_ups,_and_forms":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=poptin_exit_intent_pop_ups_and_forms"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1

        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=quickcep_‑_bot,_chat_&_email":
        # elif dvpurl == "https://apps.shopline.com/detail/?appHandle=quickcep_-_bot,_chat_&_email":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=quickcep_bot_chat_email"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=easyparcel_-_delivery_made_easy":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=easyparcel_delivery_made_easy"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=geolocation_redirects":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=duoshichangzhongdingxiang"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=pt._shippindo_teknologi_logistik":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=shipper_logistic"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=klaviyo_-_email_marketing_app":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=klaviyo_email_marketing_app"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=kua.ai":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=kua_ai"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=print_on_demand_&_dropshipping":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=print_on_demand_dropshipping"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=shopflex:_marketing&operation_automation":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=shopflex_marketing_operation_automation"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=kakaclo_-_dropshipping":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=kakaclo_dropshipping"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=miduoke_enterprise":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=miduoke"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=tec-kol:_influencer_marketing_platform":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=taikekol"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=yahoo_tracks_dot_one-click_install":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=yahoo_tracks_dot_one_click_install"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=contact_lens_bundle_purchase_plugin":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=add_to_cart_plugin_for_contact_lens"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=myyshop":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=xianzhi"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=calendar_booking-in-store_service":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=calendar_booking"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=prompt:_email_popup_&_upsell":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=prompt_email_popup_upsell"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=irobotbox-erp":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=irobotbox_erp"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=dcs_gto_file_sync":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=dcs_synchronized_data_tool"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=wininfluencer":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=hongque_kol"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=wanliniu_erp":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=niuniu_erp"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=laibot_ai_customer_service_platform":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=laibaozhineng"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=wangdiantong_cross-border":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=wangdiantong_cross_border"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=hubspot_shopline_integration":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=hubspot_by_makewebbetter"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=staff_attendance_management":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=yuangongkaoqinguanli"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=pickupp:_on‑demand_delivery":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=pickupp_on_demand_delivery"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=xcollab:_brand_collaborations":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=xcollab_brand_collaborations"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=sendcloud_shipping":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=sendcloudapp"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=eiz_fulfillment_technology":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=eiz_fulfillment"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=dowsure":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=doushabao_dowsure"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=cedcommerce_catch_integration":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=shopline_catch_integration4254"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=cedcommerce_ebay_integration":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=shopline_ebay_integration4303"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=cedcommerce_amazon_integration":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=shopline_amazon_integration4302"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=yopoun":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=youbangkeji4151"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=wemedia":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=wemediameijieguanjia"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=hs_product_options_&_variants":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=hi_options"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        elif dvpurl == "https://apps.shopline.com/detail/?appHandle=woocommerce_one_click_migration":
            dvpurl = "https://apps.shopline.com/detail/?appHandle=woocommerce"
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
        else:
            driver = webdriver.Chrome()
            driver.get(dvpurl)
            developers = driver.find_elements(By.XPATH,".//p[@class = 'body_4 color_grey1']")
            # print(developers)
            # Convert the elements to text format
            developers_texts = [developers.text for developers in developers]
            developer = developers_texts[0] #developer name
            print(developer)
            dvlls.append(developer)
            driver.close
            count+=1
            print(count)
except IndexError:
    print("web page not exits: ",count)
    
print(dvlls)
df = pd.DataFrame(dvlls)
df.to_excel('developername.xlsx',index=False)