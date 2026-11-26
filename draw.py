#!/usr/bin/env python3
"""Draw the front page for Thursday 26 November 2026 and save entry.png.

Run locally:  python3 draw.py
Output:        entry.png  (1024x1024, under 1 MiB)
The grader never runs this file; main.py only copies entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FDIR = "/usr/share/fonts/truetype/dejavu"

def font(name, size):
    return ImageFont.truetype(os.path.join(FDIR, name), size)

SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 18)
RED = (178, 34, 34)
DARKRED = (140, 20, 20)
BLUE = (24, 68, 128)
GREEN = (28, 110, 60)
AMBER = (166, 110, 0)
GREY = (110, 105, 95)
RULE = (60, 55, 48)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def text(x, y, s, f, fill=INK, anchor="la"):
    d.text((x, y), s, font=f, fill=fill, anchor=anchor)

def wrap(s, f, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 6], fill=RED)
text(20, 12, "THE WORLD IN ONE PAGE", SERIF_B(44), fill=INK)
text(1004, 24, "ONE DAY", SANS_B(13), fill=RED, anchor="ra")
text(1004, 42, "ONE PAGE", SANS_B(13), fill=RED, anchor="ra")
text(1004, 60, "ONE PICTURE", SANS_B(13), fill=RED, anchor="ra")
d.line([20, 76, 1004, 76], fill=RULE, width=2)
text(20, 82, "THURSDAY  26  NOVEMBER  2026", SANS_B(15), fill=INK)
text(1004, 82, "30 STORIES  \u2022  6 CONTINENTS  \u2022  ALL REPORTED TODAY",
     SANS_B(12), fill=INK, anchor="ra")
d.line([20, 104, 1004, 104], fill=RULE, width=3)

# ---------------------------------------------------------------- lead band
d.rectangle([20, 110, 1004, 188], fill=(255, 255, 255), outline=RULE, width=1)
d.rectangle([20, 110, 1004, 132], fill=DARKRED)
text(30, 114, "THE DAY IN ONE LINE", SANS_B(13), fill=(255, 255, 255))
text(30, 136, "HOUTHIS CLAIM HIT ON SAUDI REFINERY", SERIF_B(28), fill=INK)
text(30, 168, "Cairo tanker fire kills 31  \u2022  US unveils tariffs on 14 partners  \u2022  Nasdaq nears bear market",
     SANS_B(12), fill=INK)
# small drawn refinery + flame at right of lead band
bx, by = 890, 148
d.rectangle([bx, by + 18, bx + 104, by + 38], fill=(70, 70, 70))
for i, h in enumerate([24, 36, 28, 18]):
    d.rectangle([bx + 8 + i * 25, by + 38 - h, bx + 23 + i * 25, by + 38], fill=(90, 90, 90))
d.polygon([(bx + 13, by + 16), (bx + 21, by - 4), (bx + 29, by + 16)], fill=(255, 140, 0))
d.polygon([(bx + 17, by + 16), (bx + 21, by + 3), (bx + 25, by + 16)], fill=(255, 220, 0))
d.line([bx, by + 38, bx + 104, by + 38], fill=INK, width=2)

# ---------------------------------------------------------------- timeline
text(20, 196, "TIMELINE \u2014 26 NOVEMBER, ASIAN CLOCK (LOCAL TIMES)",
     SANS_B(11), fill=RED)
tl = [
    ("00:48 IST", "Houthis claim Ras Tanura refinery attack"),
    ("01:52 WIB", "Cairo fire toll: 31 dead on Ring Road"),
    ("MORNING IST", "India: Constitution Day; 18th 26/11 anniversary"),
    ("10:13 CST", "Shenzhou-24 docks at Tiangong"),
    ("MIDDAY AEDT", "Solomons\u2013Australia treaty signed, Canberra"),
    ("LATE, WASH.", "US unveils tariffs on 14 partners"),
]
tx = 20
for t, s in tl:
    text(tx, 212, t, SANS_B(10), fill=RED)
    for i, ln in enumerate(wrap(s, SANS(10), 150)[:2]):
        text(tx, 225 + i * 11, ln, SANS(10), fill=INK)
    tx += 168
d.line([20, 250, 1004, 250], fill=RULE, width=1)

# ---------------------------------------------------------------- stories
# (region, headline, summary, source, confidence)
STORIES = [
    ("MIDEAST", "Houthis claim Saudi refinery hit",
     "Yemen's Houthis say they struck Ras Tanura, the kingdom's biggest refinery; satellite images show black smoke. Riyadh says it downed four drones.",
     "Reuters", "CLAIM"),
    ("GULF", "Two tankers hit mines in Hormuz",
     "Iran's Revolutionary Guards say two tankers struck naval mines and caught fire in the Strait of Hormuz, on an unauthorised route.",
     "IRGC via AP", "CLAIM"),
    ("GAZA", "Israel kills Hamas security chief",
     "An Israeli strike in Gaza City kills Hamas security chief Mohammad Abuelouf, his wife and two children, medics and Gaza officials say.",
     "AP", "REPORTED"),
    ("UKRAINE", "Kyiv hits two Russian refineries",
     "Ukraine strikes two Russian oil refineries overnight, setting them ablaze; President Putin vows retaliation as the war grinds on.",
     "Reuters", "ONGOING"),
    ("RUSSIA", "Leaked data: 490,334 war dead",
     "Leaked Russian statistics show at least 490,334 soldiers have died in Ukraine; analysts say the true toll may reach 700,000.",
     "Reuters", "REPORTED"),
    ("EGYPT", "Cairo tanker fire kills 31",
     "A fuel tanker overturns on Cairo's Ring Road and explodes; at least 31 people die, 21 are hurt and 27 vehicles burn.",
     "AP", "REPORTED"),
    ("TRADE", "US unveils tariffs on 14 partners",
     "Washington proposes new tariffs on 14 economies, with an extra 20% on China, over what it calls excess factory capacity.",
     "AP", "REPORTED"),
    ("MARKETS", "Nasdaq nears bear market",
     "The Nasdaq falls 2% and sits nearly 20% below its October peak; Seoul's KOSPI plunges 6% and Tokyo's Nikkei drops 3%.",
     "Reuters", "REPORTED"),
    ("TECH", "Nvidia on downgrade watch",
     "S&P puts Nvidia on downgrade watch after the Huang exit and return; Vice-President Vance says the CEO will need no pardon.",
     "AP", "ONGOING"),
    ("TECH", "Huawei guilty on 10 of 12 counts",
     "A New York jury convicts Huawei of trade-secret theft and bank fraud; it clears the firm of racketeering. Sentencing 14 Sep 2027.",
     "Reuters", "REPORTED"),
    ("SPACE", "First Pakistani reaches Tiangong",
     "China's Shenzhou-24 docks at Tiangong with Muhammad Zeeshan Ali, the first foreign astronaut to visit the station.",
     "Reuters", "REPORTED"),
    ("PACIFIC", "Solomons pick Australia as partner",
     "The Solomon Islands sign a treaty naming Australia their primary security partner and barring any foreign military base.",
     "AP", "REPORTED"),
    ("ASIA", "N. Korea expels Swiss diplomat",
     "Pyongyang orders Switzerland to close its new office and gives its head 48 hours to leave, declaring him persona non grata.",
     "AP", "REPORTED"),
    ("SUDAN", "Drone strikes kill 19 civilians",
     "Rapid Support Forces drones hit homes in Blue Nile state, killing 19 civilians including six women, rights lawyers say.",
     "Reuters", "REPORTED"),
    ("COLOMBIA", "20 hostages freed after 17 hours",
     "Police storm a Cartagena supermarket and free 20 hostages held for 17 hours after a botched robbery; one captor is killed.",
     "BBC", "REPORTED"),
    ("INDIA", "18 years on, Mumbai remembers 26/11",
     "India marks Constitution Day and the 18th anniversary of the 2008 Mumbai attacks, with tributes across the country.",
     "Indian media", "REPORTED"),
    ("BANGLADESH", "Hasina asks to return on 16 Dec",
     "Former prime minister Sheikh Hasina asks Dhaka to arrange her return from India on 16 December.",
     "SelfStudy", "REPORTED"),
    ("BANGLADESH", "Garment wage rises 36%",
     "Bangladesh raises the minimum monthly wage for entry-level garment workers by 36%, a lift for millions in the sector.",
     "SelfStudy", "REPORTED"),
    ("NEPAL", "India offers Rs15,000-crore aid",
     "India announces a Rs15,000-crore development package for Nepal after talks between PM Modi and PM Balendra Shah.",
     "SelfStudy", "REPORTED"),
    ("CRICKET", "Boy wonder hits 204 off 53 balls",
     "Vaibhav Sooryavanshi, 15, smashes the fastest List A double century ever, with 28 sixes, as India A beat UAE in Doha.",
     "IANS", "REPORTED"),
    ("CHESS", "Gukesh draws Game 2 in Geneva",
     "World champion D. Gukesh draws Game 2 of his title defence against Uzbekistan's Javokhir Sindarov after 20 moves with white.",
     "Sportstar", "REPORTED"),
    ("CRICKET", "1,220 sign up for IPL auction",
     "A record 1,220 players register for the IPL 2027 auction; ex-England captain Ben Stokes is among the entrants.",
     "MyKhel", "REPORTED"),
    ("SCIENCE", "Asteroid test reveals new crater",
     "Close-up images from Earth's asteroid-defence test reveal a new crater on the rock deliberately struck to test deflection.",
     "BBC", "REPORTED"),
    ("HEALTH", "Mosquito trick cuts virus by 68%",
     "Releasing Wolbachia-infected mosquitoes slashes mosquito-borne viral infections by 68% in Brazil, researchers report.",
     "Studmentor", "REPORTED"),
    ("USA", "Army blows up last lead azide",
     "The US Army detonates the nation's entire stockpile of lead azide, an explosive chemical, in Iowa, calling it a success.",
     "AP", "REPORTED"),
    ("USA", "Six die in Mississippi plane crash",
     "Two children are among six killed when a plane crashes off the Mississippi coast, officials say.",
     "AP", "REPORTED"),
    ("MUSIC", "Duran Duran guitarist dies at 65",
     "Andy Taylor, guitarist of new-wave icons Duran Duran, dies aged 65.",
     "BBC", "REPORTED"),
    ("BUSINESS", "Poundland heads for administration",
     "UK discounter Poundland prepares to appoint administrators, putting 600 stores and about 12,000 jobs in doubt.",
     "Sky News", "REPORTED"),
    ("USA", "Abrego Garcia leaves for Spain",
     "Salvadoran migrant Kilmar Abrego Garcia, mistakenly deported in 2025, boards a flight from the US to Madrid.",
     "ABC News", "REPORTED"),
    ("USA", "Thanksgiving, turkeys spared",
     "America marks Thanksgiving; President Trump pardons turkeys Freedom and Feathers as an East Coast storm looms.",
     "Reuters", "REPORTED"),
]

TAG_FILL = {"REPORTED": GREEN, "CLAIM": AMBER, "ONGOING": BLUE}
text(20, 256, "THE 30 STORIES", SANS_B(13), fill=INK)
text(1004, 256, "EVERY STORY NUMBERED \u2022 SOURCE NAMED \u2022 CONFIDENCE LABELLED",
     SANS_B(10), fill=GREY, anchor="ra")
d.line([20, 274, 1004, 274], fill=RULE, width=1)

COL_X = [20, 352, 684]
COL_W = 312
ROW_H = 55
TOP = 280
for idx, (region, head, summ, src, conf) in enumerate(STORIES):
    col = idx // 10
    row = idx % 10
    x = COL_X[col]
    y = TOP + row * ROW_H
    # number + region + confidence tag
    text(x, y, "%02d" % (idx + 1), SANS_B(11), fill=RED)
    text(x + 25, y, region, SANS_B(10), fill=BLUE)
    tw = d.textlength(" " + conf + " ", font=SANS_B(8))
    d.rectangle([x + COL_W - tw - 2, y + 1, x + COL_W, y + 11], fill=TAG_FILL[conf])
    text(x + COL_W - tw / 2 - 1, y + 1, conf, SANS_B(8), fill=(255, 255, 255), anchor="ma")
    # headline (1 line, shrink if needed)
    hf = SANS_B(11)
    while d.textlength(head, font=hf) > COL_W and hf.size > 9:
        hf = SANS_B(hf.size - 1)
    text(x, y + 13, head, hf, fill=INK)
    # summary (2 lines)
    for i, ln in enumerate(wrap(summ, SANS(9), COL_W)[:2]):
        text(x, y + 25 + i * 10, ln, SANS(9), fill=(40, 40, 40))
    # source
    text(x, y + 45, "Source: " + src, SANS(8), fill=GREY)

# ---------------------------------------------------------------- bottom band
BY = 842
d.line([20, BY - 8, 1004, BY - 8], fill=RULE, width=2)

# Panel A: world map
text(20, BY, "WHERE IT HAPPENED", SANS_B(12), fill=INK)
text(20, BY + 15, "Each dot: a story on this page. Schematic map, not to scale.",
     SANS(9), fill=GREY)
MX0, MY0, MX1, MY1 = 28, BY + 30, 352, BY + 156
d.rectangle([MX0, MY0, MX1, MY1], fill=(214, 230, 240), outline=RULE, width=1)

def proj(lon, lat):
    px = MX0 + (lon + 170.0) / 360.0 * (MX1 - MX0)
    py = MY0 + (75.0 - lat) / 133.0 * (MY1 - MY0)
    return (px, py)

CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 70), (-75, 62),
     (-60, 55), (-55, 47), (-70, 42), (-75, 35), (-80, 26), (-90, 21), (-97, 16),
     (-105, 20), (-115, 28), (-125, 40), (-125, 49), (-140, 60), (-165, 60)],
    [(-80, 10), (-75, 0), (-70, -10), (-60, -20), (-50, -30), (-40, -25), (-35, -8),
     (-45, 0), (-55, 5), (-65, 10), (-75, 12)],
    [(-10, 36), (-5, 43), (0, 50), (5, 55), (10, 58), (20, 60), (25, 65), (30, 70),
     (40, 68), (45, 60), (40, 55), (35, 50), (30, 45), (25, 40), (20, 38), (10, 38), (0, 36)],
    [(-17, 15), (-10, 30), (0, 35), (10, 37), (20, 32), (30, 31), (35, 28), (40, 15),
     (48, 11), (51, 10), (45, 0), (40, -10), (35, -20), (30, -30), (20, -35),
     (15, -30), (12, -18), (9, -5), (9, 4), (-8, 5), (-15, 10)],
    [(40, 68), (60, 70), (80, 73), (100, 76), (120, 73), (140, 72), (160, 70),
     (170, 66), (160, 60), (140, 55), (130, 45), (127, 40), (120, 30), (110, 20),
     (105, 10), (100, 8), (95, 15), (90, 22), (85, 20), (80, 10), (75, 8),
     (70, 20), (60, 25), (55, 28), (50, 30), (45, 35), (40, 40), (35, 45), (30, 42)],
    [(113, -22), (120, -14), (130, -12), (135, -12), (142, -11), (146, -19),
     (150, -22), (153, -27), (150, -37), (140, -38), (130, -32), (120, -34), (114, -30)],
]
for poly in CONTINENTS:
    d.polygon([proj(lon, lat) for lon, lat in poly], fill=(190, 195, 185),
              outline=(90, 95, 90))
PINS = [(50, 26.6), (56.5, 26.5), (34.5, 31.5), (30.5, 50.4), (37.6, 55.7),
        (31.2, 30.0), (-77, 38.9), (116.4, 39.9), (149.1, -35.3), (77.2, 28.6),
        (51.5, 25.3), (-75.5, 10.4), (34.5, 11.8), (125.8, 39.0), (6.1, 46.2),
        (-0.1, 51.5), (-89, 30.2), (90, 23.8)]
for lon, lat in PINS:
    px, py = proj(lon, lat)
    d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED, outline=(255, 255, 255))

# Panel B: the day in numbers
NX = 372
text(NX, BY, "THE DAY IN NUMBERS", SANS_B(12), fill=INK)
NUMBERS = [
    ("31", "killed in the Cairo tanker fire"),
    ("550,000", "barrels a day at Ras Tanura"),
    ("490,334", "Russian war dead, leaked data"),
    ("20%", "extra US tariff on China"),
    ("204", "runs off 53 balls, Sooryavanshi, 15"),
    ("6%", "KOSPI's one-day plunge"),
    ("1,220", "players in the IPL 2027 auction"),
    ("36%", "Bangladesh garment wage rise"),
    ("17", "hours of the Colombia siege"),
    ("19", "civilians killed in Sudan"),
]
for i, (n, s) in enumerate(NUMBERS):
    yy = BY + 18 + i * 13
    text(NX, yy, n, SANS_B(11), fill=RED)
    text(NX + 78, yy, s, SANS(10), fill=INK)

# Panel C: date check + how sure + also on
CX = 696
text(CX, BY, "DATE CHECK", SANS_B(12), fill=RED)
dc = ("Every story here was first reported on Thu 26 Nov 2026 in at least "
      "one timezone. Struck out: Amazon-Decart (23 Nov); Nvidia CEO "
      "resignation (12 Nov); Huawei trial start (2019); 26/11 attacks "
      "(2008, today is the 18th anniversary).")
for i, ln in enumerate(wrap(dc, SANS(9), 308)):
    text(CX, BY + 18 + i * 11, ln, SANS(9), fill=INK)
yy = BY + 18 + len(wrap(dc, SANS(9), 308)) * 11 + 6
text(CX, yy, "HOW SURE", SANS_B(11), fill=INK)
yy += 14
hs = "REPORTED = confirmed by the named source.  CLAIM = one side's claim, not verified.  ONGOING = still developing."
for ln in wrap(hs, SANS(9), 308):
    text(CX, yy, ln, SANS(9), fill=INK)
    yy += 11
yy += 4
text(CX, yy, "ALSO ON 26 NOVEMBER", SANS_B(11), fill=INK)
yy += 14
ALSO = [
    "Malaysia sues Google for $146m (Reuters)",
    "Indonesia mine flood kills nine (reports)",
    "UAE bus crash kills 13 workers (reports)",
]
for a in ALSO:
    text(CX, yy, "\u2022  " + a, SANS(9), fill=INK)
    yy += 11

# ---------------------------------------------------------------- footer
d.line([20, 1006, 1004, 1006], fill=RULE, width=1)
text(20, 1012, "THE WORLD IN ONE PAGE \u2022 THURSDAY 26 NOVEMBER 2026 \u2022 Sources named on every story. Claims labelled, never stated as fact.",
     SANS(8), fill=GREY)
text(1004, 1012, "30 STORIES", SANS_B(8), fill=RED, anchor="ra")

out = os.path.join(HERE, "entry.png")
img.save(out, optimize=True)
print("saved", out, os.path.getsize(out), "bytes", img.size)
