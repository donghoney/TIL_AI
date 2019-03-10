## 주가예측에 필요한 데이터 선정

### Market data

The data includes a subset of US-listed instruments. The set of included instruments changes daily and is determined based on the amount traded and the availability of information. This means that there may be instruments that enter and leave this subset of data. There may therefore be gaps in the data provided, and this does not necessarily imply that that data does not exist (those rows are likely not included due to the selection criteria).

The marketdata contains a variety of returns calculated over different timespans. All of the returns in this set of marketdata have these properties:

- Returns are always calculated either open-to-open (from the opening time of one trading day to the open of another) or close-to-close (from the closing time of one trading day to the open of another).
- Returns are either raw, meaning that the data is not adjusted against any benchmark, or market-residualized (Mktres), meaning that the movement of the market as a whole has been accounted for, leaving only movements inherent to the instrument.
- Returns can be calculated over any arbitrary interval. Provided here are 1 day and 10 day horizons.
- Returns are tagged with 'Prev' if they are backwards looking in time, or 'Next' if forwards looking.

Within the marketdata, you will find the following columns:

- `time`(datetime64[ns, UTC]) - the current time (in marketdata, all rows are taken at 22:00 UTC)
- `assetCode`(object) - a unique id of an asset
- `assetName`(category) - the name that corresponds to a group of `assetCodes`. These may be "Unknown" if the corresponding `assetCode` does not have any rows in the news data.
- `universe`(float64) - a boolean indicating whether or not the instrument on that day will be included in scoring. This value is not provided outside of the training data time period. The trading universe on a given date is the set of instruments that are avilable for trading (the scoring function will not consider instruments that are not in the trading universe). The trading universe changes daily.
- `volume`(float64) - trading volume in shares for the day
- `close`(float64) - the close price for the day (not adjusted for splits or dividends)
- `open`(float64) - the open price for the day (not adjusted for splits or dividends)
- `returnsClosePrevRaw1`(float64) - see returns explanation above
- `returnsOpenPrevRaw1`(float64) - see returns explanation above
- `returnsClosePrevMktres1`(float64) - see returns explanation above
- `returnsOpenPrevMktres1`(float64) - see returns explanation above
- `returnsClosePrevRaw10`(float64) - see returns explanation above
- `returnsOpenPrevRaw10`(float64) - see returns explanation above
- `returnsClosePrevMktres10`(float64) - see returns explanation above
- `returnsOpenPrevMktres10`(float64) - see returns explanation above
- **returnsOpenNextMktres10(float64) - 10 day, market-residualized return. This is the target variable used in competition scoring. The market data has been filtered such that returnsOpenNextMktres10 is always not null.**

### News data

The news data contains information at both the news article level and asset level (in other words, the table is intentionally not normalized).

- `time`(datetime64[ns, UTC]) - UTC timestamp showing when the data was available on the feed (second precision)

- `sourceTimestamp`(datetime64[ns, UTC]) - UTC timestamp of this news item when it was created

- `firstCreated`(datetime64[ns, UTC]) - UTC timestamp for the first version of the item

- `sourceId`(object) - an Id for each news item

- `headline`(object) - the item's headline

- `urgency`(int8) - differentiates story types (1: alert, 3: article)

- `takeSequence`(int16) - the take sequence number of the news item, starting at 1. For a given story, alerts and articles have separate sequences.

- `provider`(category) - identifier for the organization which provided the news item (e.g. RTRS for Reuters News, BSW for Business Wire)

- `subjects`(category) - topic codes and company identifiers that relate to this news item. Topic codes describe the news item's subject matter. These can cover asset classes, geographies, events, industries/sectors, and other types.

- `audiences`(category) - identifies which desktop news product(s) the news item belongs to. They are typically tailored to specific audiences. (e.g. "M" for Money International News Service and "FB" for French General News Service)

- `bodySize`(int32) - the size of the current version of the story body in characters

- `companyCount`(int8) - the number of companies explicitly listed in the news item in the subjects field

- `headlineTag`(object) - the Thomson Reuters headline tag for the news item

- `marketCommentary`(bool) - boolean indicator that the item is discussing general market conditions, such as "After the Bell" summaries

- `sentenceCount`(int16) - the total number of sentences in the news item. Can be used in conjunction with firstMentionSentence to determine the relative position of the first mention in the item.

- `wordCount`(int32) - the total number of lexical tokens (words and punctuation) in the news item

- `assetCodes`(category) - list of assets mentioned in the item

- `assetName`(category) - name of the asset

- ```
  firstMentionSentence
  ```

  (int16) - the first sentence, starting with the headline, in which the scored asset is mentioned.

  - 1: headline
  - 2: first sentence of the story body
  - 3: second sentence of the body, etc
  - 0: the asset being scored was not found in the news item's headline or body text. As a result, the entire news item's text (headline + body) will be used to determine the sentiment score.

- `relevance`(float32) - a decimal number indicating the relevance of the news item to the asset. It ranges from 0 to 1. If the asset is mentioned in the headline, the relevance is set to 1. When the item is an alert (urgency == 1), relevance should be gauged by firstMentionSentence instead.

- `sentimentClass`(int8) - indicates the predominant sentiment class for this news item with respect to the asset. The indicated class is the one with the highest probability.

- `sentimentNegative`(float32) - probability that the sentiment of the news item was negative for the asset

- `sentimentNeutral`(float32) - probability that the sentiment of the news item was neutral for the asset

- `sentimentPositive`(float32) - probability that the sentiment of the news item was positive for the asset

- `sentimentWordCount`(int32) - the number of lexical tokens in the sections of the item text that are deemed relevant to the asset. This can be used in conjunction with wordCount to determine the proportion of the news item discussing the asset.

- `noveltyCount12H`(int16) - The 12 hour novelty of the content within a news item on a particular asset. It is calculated by comparing it with the asset-specific text over a cache of previous news items that contain the asset.

- `noveltyCount24H`(int16) - same as above, but for 24 hours

- `noveltyCount3D`(int16) - same as above, but for 3 days

- `noveltyCount5D`(int16) - same as above, but for 5 days

- `noveltyCount7D`(int16) - same as above, but for 7 days

- `volumeCounts12H`(int16) - the 12 hour volume of news for each asset. A cache of previous news items is maintained and the number of news items that mention the asset within each of five historical periods is calculated.

- `volumeCounts24H`(int16) - same as above, but for 24 hours

- `volumeCounts3D`(int16) - same as above, but for 3 days

- `volumeCounts5D`(int16) - same as above, but for 5 days

- `volumeCounts7D`(int16) - same as above, but for 7 days

### 시장 데이터

이 데이터에는 미국에 등록 된 계측기의 하위 집합이 포함됩니다. 포함 된 수단 세트는 매일 바뀌며 거래되는 금액과 정보의 가용성에 따라 결정됩니다. 즉, 데이터의 하위 집합으로 들어오고 나가는 도구가있을 수 있습니다. 따라서 제공된 데이터에 틈이있을 수 있으며, 이것이 반드시 해당 데이터가 존재하지 않는다는 것을 의미하지는 않습니다 (선택 기준으로 인해 행이 포함되지 않을 가능성이 높음).

시장 데이터에는 다른 기간에 대해 계산 된 다양한 수익률이 포함됩니다. 이 시장 데이터 집합의 모든 수익은 다음과 같은 속성을가집니다.

- 반품은 항상 열림 (1 거래일의 개장 시간에서 다른 날의 개장까지) 또는 마감 (1 거래일의 마감 시간에서 다른 영업 시간까지)으로 계산됩니다.
- 반환 값은 원시 (즉, 데이터가 벤치 마크와 비교하여 조정되지 않았 음을 의미) 또는 시장 잔여 (Mktres)로, 시장 전체의 움직임이 계측되어 계기 고유의 움직임 만 남았습니다.
- 반환 값은 임의의 간격으로 계산할 수 있습니다. 여기에 1 일 및 10 일의 시야가 제공됩니다.
- 반환 값은 거꾸로보고있는 경우 'Prev'로 표시되고, 앞으로보고 있으면 'Next'로 태그가 지정됩니다.

시장 데이터 내에서 다음 열을 찾을 수 있습니다.

- `time`(datetime64 [ns, UTC]) - 현재 시간 (시장 데이터에서 모든 행은 22:00 UTC로 찍음)
- `assetCode`(객체) - 저작물의 고유 ID
- `assetName`(category) -의 그룹에 해당하는 이름 `assetCodes`. 해당 `assetCode`하는 뉴스 데이터에 행이 없으면 '알 수 없음'일 수 있습니다 .
- `universe`(float64) - 해당 날의 측량기가 득점에 포함되는지 여부를 나타내는 부울 값입니다. 이 값은 학습 데이터 시간대 밖에서는 제공되지 않습니다. 주어진 날짜에 거래 우주는 거래에 사용할 수있는 도구 세트입니다 (채점 기능은 거래 세계에 있지 않은 도구를 고려하지 않습니다). 거래 세계는 매일 바뀝니다.
- `volume`(float64) - 당일 주식 거래량
- `close`(float64) - 당일의 마감 가격 (분할 또는 배당에 조정되지 않음)
- `open`(float64) - 당일 오픈 프라이스 (분할 또는 배당에 조정되지 않음)
- `returnsClosePrevRaw1`(float64) - 위의 반품 설명 참조
- `returnsOpenPrevRaw1`(float64) - 위의 반품 설명 참조
- `returnsClosePrevMktres1`(float64) - 위의 반품 설명 참조
- `returnsOpenPrevMktres1`(float64) - 위의 반품 설명 참조
- `returnsClosePrevRaw10`(float64) - 위의 반품 설명 참조
- `returnsOpenPrevRaw10`(float64) - 위의 반품 설명 참조
- `returnsClosePrevMktres10`(float64) - 위의 반품 설명 참조
- `returnsOpenPrevMktres10`(float64) - 위의 반품 설명 참조
- **returnsOpenNextMktres10(float64) - 10 일, 시장 잔류 수익. 이것은 경쟁 점수에서 사용되는 목표 변수입니다. 시장 데이터 returnsOpenNextMktres10가 항상 Null이 아닌 필터링되었습니다 .**

### 뉴스 데이터

뉴스 데이터에는 뉴스 기사 수준과 자산 수준의 정보가 포함됩니다 (즉, 표는 의도적으로 표준화되지 않았습니다).

- `time`(datetime64 [ns, UTC]) - 피드에서 데이터를 사용할 수 있었던 시간을 보여주는 UTC 타임 스탬프 (두 번째 정밀도)

- `sourceTimestamp`(datetime64 [ns, UTC]) -이 뉴스 항목이 생성되었을 때 UTC 타임 스탬프

- `firstCreated`(datetime64 [ns, UTC]) - 항목의 첫 번째 버전에 대한 UTC 타임 스탬프

- `sourceId`(객체) - 각 뉴스 항목의 ID

- `headline`(객체) - 항목의 제목

- `urgency`(int8) - 스토리 유형 구분 (1 : 경고, 3 : 기사)

- `takeSequence`(int16) - 1에서 시작하는 뉴스 항목의 테이크 시퀀스 번호. 특정 스토리의 경우 경고 및 기사에는 별도의 순서가 있습니다.

- `provider`(카테고리) - 뉴스 항목을 제공 한 조직의 식별자 (예 : 로이터 뉴스의 경우 RTRS, 비즈니스 와이어의 경우 BSW)

- `subjects`(카테고리) -이 뉴스 항목과 관련된 주제 코드 및 회사 식별자. 주제 코드는 뉴스 항목의 주제를 설명합니다. 여기에는 자산 클래스, 지역, 이벤트, 업종 / 부문 및 기타 유형이 포함됩니다.

- `audiences`(카테고리) - 뉴스 항목이 속한 데스크톱 뉴스 제품을 식별합니다. 일반적으로 특정 잠재 고객에게 맞춰집니다. (예 : Money International News Service의 경우 "M", 프랑스 일반 뉴스 서비스의 경우 "FB")

- `bodySize`(int32) - 스토리 본문의 현재 버전 크기 (문자)

- `companyCount`(int8) - 주제 필드의 뉴스 항목에 명시 적으로 나열된 회사 수

- `headlineTag`(객체) - 뉴스 항목의 Thomson Reuters 헤드 라인 태그

- `marketCommentary`(bool) - 아이템이 "After the Bell"요약과 같은 일반적인 시장 조건을 논의하고 있음을 나타내는 부울 지시자

- `sentenceCount`(int16) - 뉴스 항목의 총 문장 수입니다. firstMentionSentence와 함께 사용하여 항목의 첫 번째 언급의 상대적 위치를 결정할 수 있습니다.

- `wordCount`(int32) - 뉴스 항목의 어휘 토큰 (단어 및 구두점)의 총 수

- `assetCodes`(카테고리) - 항목에 언급 된 자산 목록

- `assetName`(카테고리) - 자산의 이름

- ```
  firstMentionSentence
  ```

  (int16) - 점수가 매겨진 자산이 언급 된 헤드 라인으로 시작하는 첫 번째 문장.

  - 1 : 광고 제목
  - 2 : 이야기 본문의 첫 번째 문장
  - 3 : 몸의 두 번째 문장 등
  - 0 : 점수가 매겨진 자산이 뉴스 항목의 제목 또는 본문 텍스트에서 발견되지 않았습니다. 결과적으로 전체 뉴스 항목의 텍스트 (헤드 라인 + 본문)가 정서 점수를 결정하는 데 사용됩니다.

- `relevance`(float32) - 뉴스 항목과 자산의 관련성을 나타내는 십진수입니다. 자산이 헤드 라인에 언급 된 경우 관련성은 1로 설정됩니다. 항목이 경고 (긴급 == 1) 인 경우 관련성은 firstMentionSentence에 의해 대신 측정되어야합니다.

- `sentimentClass`(int8) - 자산과 관련된이 뉴스 항목의 주된 정서 클래스를 나타냅니다. 표시된 클래스는 가장 높은 확률을 가진 클래스입니다.

- `sentimentNegative`(float32) - 뉴스 항목의 정서가 자산에 대해 부정적 일 확률

- `sentimentNeutral`(float32) - 뉴스 항목의 정서가 자산에 대해 중립적 일 확률

- `sentimentPositive`(float32) - 뉴스 항목의 정서가 자산에 긍정적이었을 확률

- `sentimentWordCount`(int32) - 항목 텍스트의 섹션에서 해당 자산과 관련 있다고 생각되는 어휘 토큰 수입니다. 이는 wordCount와 함께 사용하여 자산을 논의하는 뉴스 항목의 비율을 결정할 수 있습니다.

- `noveltyCount12H`(int16) - 특정 자산의 뉴스 항목에있는 내용의 12 시간 참신. 자산이 포함 된 이전 뉴스 항목의 캐시를 통해 자산 별 텍스트와 비교하여 계산됩니다.

- `noveltyCount24H`(int16) - 위와 동일하지만 24 시간 동안

- `noveltyCount3D`(int16) - 위와 같지만 3 일 동안

- `noveltyCount5D`(int16) - 위와 같지만 5 일 동안

- `noveltyCount7D`(int16) - 위와 동일하지만 7 일 동안

- `volumeCounts12H`(int16) - 각 자산에 대한 12 시간 분량의 뉴스. 이전 뉴스 항목의 캐시가 유지되며 5 개의 과거 기간마다 자산을 언급하는 뉴스 항목 수가 계산됩니다.

- `volumeCounts24H`(int16) - 위와 동일하지만 24 시간 동안

- `volumeCounts3D`(int16) - 위와 같지만 3 일 동안

- `volumeCounts5D`(int16) - 위와 같지만 5 일 동안

- `volumeCounts7D`(int16) - 위와 동일하지만 7 일 동안

