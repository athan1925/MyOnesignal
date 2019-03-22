from onesignal import OneSignal, SegmentNotification

client = OneSignal("b3084414-6c15-4cb1-98ee-d72c42fbe20b", "ZjhmMmFiNGQtY2E3MC00YTY4LTg1NWEtMDQ0OTJkNjQ1NTAy")
notification_to_all_users = SegmentNotification(
    contents={
        "en": "Cebu Pacific Payday Promo for as low as P199 base fare! Travel May – Sept 2019"
    },
    included_segments=SegmentNotification.ALL,
    url="https://www.redpisofare.com/2019/03/cebu-pacific-payday-promo-for-as-low-as-p199-base-fare-travel-may-sept-2019.html"
)
client.send(notification_to_all_users)