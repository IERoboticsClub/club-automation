import random

def load_pow_mail_template(
    pow_choice_name = "Attention is all you need",
    pow_choice_link = "https://arxiv.org/abs/1706.03762",
    pow_link = "https://ieconnects.ie.edu/feeds?type=club&type_id=300003041&tab=events",
    pow_date = "Thursday, 17:00-18:00",
    pow_location = "IE Tower, Floor 5"):

    # Load the PoW mail template. All inputs should be strings already formatted.

    gif_urls = [
        "https://i.gifer.com/7AJp.gif", # robot fast reading
        "https://c.tenor.com/JNvdIis2zwMAAAAC/tenor.gif", # Guy on the toilet, could be removed, but it's funny
        "https://64.media.tumblr.com/1fbaa2324986f75911fb10c40a888881/tumblr_n159v2hhu31tq4of6o1_500.gif",
        "https://daily.stillweb.org/wp-content/uploads/sites/3/2016/04/tdd-speed-reading-apps.gif",
        "https://www.connecticuthealth.com/wp-content/uploads/2016/08/speed-reading-eyes.gif?w=1080",
        "https://c.tenor.com/TwErbvrM4pAAAAAC/tenor.gif", # Did you read it?
        "https://c.tenor.com/XLhQlp7JsIwAAAAC/tenor.gif", # read the book
        "https://c.tenor.com/kAgykndiH9sAAAAC/tenor.gif", # you should read it, its good
        ]
    
    gif_choice = random.choice(gif_urls)

    # Its easier to write the mail on the IE Connects editor and paste it here
    message = f"""
<div style="max-width: 600px; margin: auto; background: #e0f7fa; padding: 50px; text-align: center; border-radius: 5px; color: #0277bd;">
<h1 style="text-align: center; font-size: 24px; margin-bottom: 20px; color: #0277bd;">💥 PoW next week has been elected! 💥</h1>

<p style="font-size: 16px; color: #0277bd; line-height: 1.5;">This week&#39;s poll in <a href="https://discord.gg/3RBZ37KYFa" style="color: #16085c; text-decoration: none;">Discord</a> has closed a vote! The next PoW will be:</p>

<h1 style="text-align: center; font-size: 24px; margin-bottom: 20px; color: #0277bd;"><a href="https://discord.gg/3RBZ37KYFa" style="color: #16085c; text-decoration: none;"><a href="{pow_choice_link}" style="color: #16085c; text-decoration: none;">{pow_choice_name}</a></h1>

<img alt="Robotics Club Gif" src="{gif_choice}" style="width: 50%;" />
<p style="font-size: 16px; color: #0277bd; line-height: 1.5;"><strong>Event Details</strong>: 📅 {pow_date} 📍 {pow_location}</p>

<div><button onclick="window.open('{pow_link}', '_blank')" style="background-color: #13aa52; border: 1px solid #13aa52; border-radius: 4px; box-shadow: rgba(0, 0, 0, .1) 0 2px 4px 0; box-sizing: border-box; color: #fff; cursor: pointer; font-family: 'Akzidenz Grotesk BQ Medium', -apple-system, BlinkMacSystemFont, sans-serif; font-size: 16px; font-weight: 400; outline: none; padding: 10px 25px; text-align: center; transition: transform 150ms, box-shadow;" type="button">Register here</button></div>
&nbsp;

<p style="font-size: 16px; color: #0277bd; line-height: 1.5;">📚 In this <strong>Paper of the Week (PoW)</strong> event, we will discuss the most interesting aspects of the chosen topic in depth.</p>

<p style="font-size: 16px; color: #0277bd; line-height: 1.5;">🙋🏻&zwj;♂️ If you have a passion for AI or a general interest in robotics and wish to learn more, you are welcome to join the discussion as an active participant or simply listen in without any obligation.</p>

<p style="font-size: 16px; color: #0277bd; line-height: 1.5;">❓ Any doubts that may arise during the reading will be addressed.</p>
&nbsp;

<div style="background-color: #0288d1; color: white; padding: 10px; border-radius: 5px; text-align: center; margin-top: 20px;">
<p style="font-size: 16px; color: white; line-height: 1.5;">Have any questions or ideas? Feel free to reach out on <a href="https://discord.gg/3RBZ37KYFa" style="color: #16085c; text-decoration: none;">Discord</a> or <a href="https://chat.whatsapp.com/JjCfGnAE0yc7xkzUR0EeHE" style="color: #16085c; text-decoration: none;">WhatsApp</a>.</p>
</div>
</div>
"""

    return message