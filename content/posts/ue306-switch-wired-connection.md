---
title: "닌텐도 스위치 유선 연결, UE306을 사기 전에 독부터 봐요"
description: "스위치 독에 LAN 포트가 있으면 어댑터를 살 필요가 없어요. LAN 포트가 없는 독에서 UE306을 연결하고 유선 인터넷을 설정하는 순서를 안내해요."
date: 2026-10-27T21:25:09.937Z
draft: false
---

이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.

독에 LAN 포트가 있으면 UE306은 필요 없어요. 공유기와 독을 랜케이블로 바로 연결하면 돼요. 독에 LAN 포트가 없으면 UE306처럼 Switch 연결을 지원하는 USB LAN 어댑터가 필요해요.

직접 사용한 후기가 아니에요. TP-Link 공식 제품 자료와 Nintendo 공식 지원 문서를 대조해 정리했어요.

## 독 뒷면부터 보세요

LAN 포트가 있는 독이라면 공유기 LAN 포트와 독을 랜케이블로 연결해요. 이 경우 USB LAN 어댑터를 따로 살 이유가 없어요.

LAN 포트가 없는 독이라면 USB LAN 어댑터를 독의 USB 포트에 꽂아야 유선으로 연결할 수 있어요.

## UE306은 어디에 꽂나요

UE306은 USB-A 단자를 랜 포트로 바꾸는 어댑터예요. TP-Link는 이 제품을 Nintendo Switch 독의 USB 포트에 꽂아 유선 LAN 연결에 쓸 수 있다고 안내해요.

연결은 이렇게 해요. UE306을 독의 USB 포트에 꽂아요. UE306의 랜 포트와 공유기를 랜케이블로 이어요. 그다음 Switch를 독에 올려요.

```text
[공유기 LAN]
     │ 랜케이블
[UE306] ── USB-A ── [LAN 포트 없는 독]
                            │
                      [Nintendo Switch]
```

{{< product-card name="티피링크 USB3.0 A타입 기가비트 유선 랜 카드 UE306 bor15jrd" image="https://ads-partners.coupang.com/image1/zAu0Gz3ZGfAoVYnczCghxTwdqiUXYMGeTTU06m7UHfSpkTgay5MYSz6vfTSN2yhZ3qfni1BQqF7j1XxhRZbMdJMrZKW_trK2uIwQ5EeUnSAueTzIuFgBC8_YJ1SlZI_zEFvSd_V9Y0GvAYHOmaEUEySeJ3kzhuA6HPEnZQlh-aN_N7gCgnVFXw6_J9s9EEmIBAozh2AN9KHYPNdKsQQA6ld9ZaCLPThtpHl5fNOrLvYYsJBV4AIK1Shp3hAOJu3W2mGruWdeMfM3pHNmPw_-jJSCrn0n1CJvOb9nHlr0sQnvElY1S2zDUzjYWu7dlI8kSEuJ3FgfSiw7tcBgdkNK32lOfnq_r17Cj7x_k1xXOtqyWhXDg5iCcbDUPUX8Unx53iODvGB1k7ZrYPTGqwHY_q1rtQcAkQtcI4p56xr9l7Y_RS7fjCXVNgfx-ycvhf0iSDbdkyJHBJWZV7A5y93r1WpVXtP6Ux2Kh_bkDduFywrg6Ylz-QZKHHI9tiUALkUvOOdaDOoW-gvVYhwoWQGRDq2edEExxpzDKteVFWD8c5Ls-vC7Q4hZhISERA==" alt="티피링크 USB3.0 A타입 기가비트 유선 랜 카드 UE306 bor15jrd 상품 이미지" url="https://link.coupang.com/re/AFFSDP?lptag=AF7582278&subid=rijeongblog&pageKey=9750643677&itemId=29196402489&vendorItemId=96116998238&traceid=V0-153-104ffd26485d5705&requestid=20261028061939521143499917&token=31850C%7CGM&pt=0&slot=2" source="https://www.nintendo.com/en-gb/Support/Troubleshooting/How-to-Connect-to-the-Internet-Using-a-Wired-Connection-1228928.html" summary="Nintendo Switch 독의 USB 포트에 연결하는 유선 랜 어댑터예요. LAN 포트가 이미 있는 독이라면 추가 구매하지 않아도 돼요." >}}

## 설정 메뉴는 이 순서예요

설정(System Settings) → 인터넷(Internet) → 인터넷 설정(Internet Settings) → 유선 연결(Wired Connection) → 유선으로 인터넷에 연결(Connect to the Internet via Wired Connection) 순서로 들어가요.

연결 테스트가 끝나면 OK를 눌러 마쳐요. 연결에 실패하면 화면에 오류 코드와 메시지가 나와요. 이 코드를 그대로 적어 두면 원인을 찾을 때 기준으로 쓸 수 있어요.

## 연결 뒤에는 테스트 결과를 봐요

기가비트는 UE306 랜 포트의 규격이에요. 실제 게임 속도나 핑을 보장하는 숫자가 아니에요. 유선으로 바꾼다고 해서 무조건 빨라지거나 지연이 해결된다고 볼 수는 없어요.

[다른 기기의 USB 연결도 고른다면 충전 전력과 데이터 규격의 차이를 확인하세요.](/posts/usb-c-cable-guide/)

자료: [제조사 제품 안내](https://www.tp-link.com/ca/home-networking/usb-hub/ue306/) · [공식 사용 안내](https://www.nintendo.com/en-gb/Support/Troubleshooting/How-to-Connect-to-the-Internet-Using-a-Wired-Connection-1228928.html)
