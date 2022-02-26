# otoshimono
落とし物共有SNS

https://otoshimono-app.herokuapp.com/

## 開発背景

- 道でマフラーやハンカチが落ちていることがある。財布が落ちている場合は流石に警察に届けるが、貴重品でない場合は届けることはない
- 落ちたまま踏まれてしまうのは心苦しいが、良かれと思って道の脇にかけてしまうと、落とし主が見つけにくくなってしまう。また、貴重品でないものが交番まで届けられている可能性も考えないので交番まで行かない。
- 個人的な体験として、この前落としたイヤリングを元来た道を辿って探したが、見つかったときには車に轢かれて無惨な姿になっていた。高価なものではないがとても悲しかった。
- 高価なものでなくても、人によっては思い出が詰まったものもある。予期せぬ悲しい別れを減らしたい。

## できること

### 落とし物を見つけた人

- 落とし物の写真、見つけた場所、届け先を登録できる
- 持ち主に届いたら通知が来る（嬉しい）

### 落とし物を落とした人

- 落とし物情報を閲覧できる
- 受け取ったら受け取ったボタンを押す
- 落とした心当たりのある場所に、探してます情報を載せられる（猫ちゃん探してますビラのイメージ）

## 懸念点

- いくらでも荒らせてしまう。
    - 落とし物情報として不適切な画像をアップする
    - 他人の落とし物情報を見て盗みに行く
    - 落とし物受け取ったボタンを勝手におす
    
    →この世の中が優しさに溢れていると信じたい
    

## 参考にしたサイト

- [https://docs.djangoproject.com/ja/4.0/intro/tutorial01/](https://docs.djangoproject.com/ja/4.0/intro/tutorial01/)
- [https://note.com/shinya_hd/n/n8de567cd82a4](https://note.com/shinya_hd/n/n8de567cd82a4)
- [https://note.com/daikinishimatsu/n/n1fc3d39694ae](https://note.com/daikinishimatsu/n/n1fc3d39694ae)
- [https://tutorial.djangogirls.org/ja/template_extending/](https://tutorial.djangogirls.org/ja/template_extending/)

## 開発予定

- Django入門
- 情報の登録と閲覧ができるサイトをデプロイする
- 受け取りボタン、それによる情報のアーカイブ実装
- 見た目をちゃんとする


## 初回起動方法

```
python -m venv venv
source venv/bin/activate
pip3 install requirements.txt
python manage.py migrate
python manage.py runserver
```

## 起動方法

```
source venv/bin/activate
python manage.py runserver
```
