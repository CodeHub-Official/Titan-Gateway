import os

def price_assets():
    # الأكواد الذهبية (الأعلى سعراً)
    top_tier_countries = ['AE', 'DE', 'CH', 'US', 'SA', 'GB']
    tech_giants = ['google', 'microsoft', 'facebook', 'banquemisr', 'credit-suisse']
    
    inventory = {'Tier_SSS': [], 'Tier_SS': [], 'Tier_S': [], 'Tier_A': []}
    
    # 1. تصنيف البنوك
    if os.path.exists('FINAL_BANKING_AUCTION.txt'):
        with open('FINAL_BANKING_AUCTION.txt', 'r') as f:
            for line in f:
                content = line.strip()
                # إذا كان الحساب من دولة غنية، فهو SSS
                if any(country in content for country in top_tier_countries):
                    inventory['Tier_SSS'].append(f"[🏦 BANK] {content} | EST. VALUE: $500")
                else:
                    inventory['Tier_S'].append(f"[🏦 BANK] {content} | EST. VALUE: $150")

    # 2. تصنيف السيرفرات (التقني)
    if os.path.exists('FINAL_TECH_EXCHANGE.txt'):
        with open('FINAL_TECH_EXCHANGE.txt', 'rb') as f:
            for line in f:
                try:
                    content = line.decode('utf-8', errors='ignore').strip()
                    if any(giant in content.lower() for giant in tech_giants):
                        inventory['Tier_SS'].append(f"[🌐 TECH] {content} | EST. VALUE: $1,000/Bundle")
                    else:
                        inventory['Tier_A'].append(f"[🌐 TECH] {content} | EST. VALUE: $50")
                except: continue

    # 3. كتابة تقرير الأرباح النهائي
    with open('MASTER_REVENUE_PLAN.txt', 'w') as r:
        r.write("=== 👑 THE IMPERIAL REVENUE MASTER PLAN 👑 ===\n\n")
        for tier in ['Tier_SSS', 'Tier_SS', 'Tier_S', 'Tier_A']:
            r.write(f"--- {tier} (High Priority to Low) ---\n")
            # كتابة أول 20 عنصر فقط من كل فئة لمنع تضخم الملف
            for item in inventory[tier][:20]:
                r.write(f"{item}\n")
            r.write(f"... and {len(inventory[tier]) - 20} more assets in this tier.\n\n")

    print("\033[1;32m[💰] REVENUE PLAN GENERATED: MASTER_REVENUE_PLAN.txt\033[0m")
    print(f"\033[1;36m[📊] SSS Assets: {len(inventory['Tier_SSS'])} | SS Assets: {len(inventory['Tier_SS'])}\033[0m")

price_assets()
