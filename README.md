## auto_like_instagram
インスタの自動いいねをするシステムを作りました。 
## 作った経緯
お世話になっている先輩が新しく事業を始める際に、「インスタでいいねを自動で押してくれるシステムを作って欲しい」と依頼されて作りました。
## 内容
[Instagram Graph API](https://developers.facebook.com/docs/instagram-api)で新規投稿のurlを取得。  
Seleniumでインスタのログインといいね、という流れになっています。  
Lambdaにデプロイしており、1時間おきに定期実行されるようになっています。  
タグを３種類用意しており、最大で25件いいねするようなシステムになっています。
## 使用技術
- python 3.8.2
- [Selenium](https://www.selenium.dev/)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api)
- AWS Lambda
