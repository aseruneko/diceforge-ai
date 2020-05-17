# 身内向け手引書

## Q. このwebサイト（github）は何ですか？

A.
>GitHub（ギットハブ）は、ソフトウェア開発のプラットフォームであり、ソースコードをホスティングする。

githubはgitを使用し、基本的にフリーで提供されているウェブサービスです。githubとgitの関係はwikipediaとwikiのそれに近いです。

主な利用目的は、共同で何か同じファイルを触る場合に、「**新しいファイル(5)_20200403_これが最新_改訂しました_最終版**」のような物を存在させることなく、うまくやるためです。

## Q. githubはどのように使いますか？

全体的な使い方は以下とかを参照。

[今さら聞けない！GitHubの使い方【超初心者向け】](
https://techacademy.jp/magazine/6235)

### 今回参加するための手順（windows）

#### 1.gitをインストールする

以下のサイトからgitをインストールします。

<https://gitforwindows.org/>

巷に転がってるインストールの手順を参照してもいいですが、軽く見てみると最初から複雑なことをやろうとしてる記事が多かったのであんまり参照しないほうがいいと思います。

#### 2.コマンドプロンプトを起動する

>まず、［Windows］＋［R］キーを押し、［ファイル名を指定して実行］ダイアログを開く。 次に［名前］入力ボックスに「cmd」と入力して、［Enter］キーを押すか、［OK］ボタンをクリックすると、コマンドプロンプトが起動する。

#### 3.Gitのパスが通っているかを確認する

コマンドプロンプト上で

`git --version`

以下のようなものがでれば成功

`git version 2.25.0.windows.1`

#### 4.オンライン上のデータを自分のPC内にコピーしgitで管理させる

コマンドプロンプト上で

`git clone https://github.com/aseruneko/diceforge-ai.git`

ディレクトリの設置場所を調整したい人はwindowsの場合、cd（階層の移動）とdir（現在いる階層のファイルとディレクトリ一覧を表示）を駆使して移動してから上記コマンドを打ってください。

#### 5.自分用の作業フォルダを作る

先程のコマンドを打った状態からコマンドプロンプトで（以下はhogeという作業フォルダを作る場合）

`cd diceforge-ai`

diceforge-aiディレクトリに移動します

`git branch hoge`

git上でhogeという名前の個人用の作業スペース（branchと言います）を作ります

`git checkout hoge`

先程作ったbranchに切り替えます（デフォルトでいるのはmaster branch）

#### 6.作業する

この状態でdiceforge-aiフォルダをVS Codeなどで開き、作業を行います。

ここではテストとして、空のテキストファイルを作成します。

先程の状態からコマンドプロンプト上で

`copy nul test.txt`

#### 7.作業した内容をアップロードする

作業した内容をアップロードし、他の人から閲覧できる状態にします。

`git add .`

gitで管理されているファイルのうち、変更があったものを検知します。

`git commit -m "test commit"`

先程検知されたファイルをcommitという単位にまとめ、「test commit」というコメントをつけます。

`git push`

先程まとめられたcommitをweb上にアップロードします（pushします）。ここでログインが求められる...はず...

#### 8.push成功の確認

<https://github.com/aseruneko/diceforge-ai/tree/hoge>

上記のURL（hogeを自分で作成したbranchの名前に差し替えてください）にアクセスし、先程作成したtest.txtが存在していれば成功。

#### 9.(optional)web上の master branchが更新されたっぽいので自分のPC内にも反映する

`git checkout master`

`git pull`

#### 10.(optional)自分のPC内のhoge branchに自分のPC内のmaster branchの内容を統合する

`git checkout hoge`

`git merge master`

#### 11.(optional)自分が作成しアップロードしたhoge branchの内容をmaster branchに取り込むよう要求する

pull requestと言います。

以下にアクセスし、newボタンから要求してください。

<https://github.com/aseruneko/diceforge-ai/pulls>

※実際、今回は全員にcollaborator権限を付与しているので、自分のPC内でmaster branchを変更してgit push -fでもすればWeb上のmaster branchを変更できますが、ver管理が面倒なのでやめてください。

## Q. 今回のゴールはなんですか？

* みんなで、DiceForgeのAIを作成し、自分の実績に加える。
* 俺が、githubとpythonと共同開発の経験を積みたく、折角なのでみんなを巻き込んでみんなでやりませんかという話
* BGAは当然なんらかの外部操作用のAPIを提供しているわけではないので → 現在のボード情報を入力した場合に次に取るべき最善手を提示してくれる状態を目指す。（もちろん画面をキャプチャして自動判定できればもっといいね）

## Q. なんで俺たちが協力しないといけないんですか？

仲間だから

## Q. それで俺たちは何をすればいいんですか？

* 一番やってくれると嬉しいのは開発に参加すること

* 二番目にやってくれると嬉しいのはコードレビューやバグを発見すること

* 三番目にやってくれると嬉しいのは一緒にdiceforgeを遊ぶこと

## Q. 俺たちになんのメリットがありますか？

* 完成したら自分の経歴に書けるよ！
* 技術力があがるよ！

## Q. 開発に参加したいが、具体的にどうすればいいんだ？

githubにはissuesという機能があります。

<https://github.com/aseruneko/diceforge-ai/issues>

掲示板のようなものです。Newから新しい目標を作成してください。

このとき、画面右にassigneeで自分を割り当ててください（問題点だけ考えて作業は僕になげてもいいですが）

## Q. pythonがわからない

俺もわからないので一緒にやろ

## Q. ○○がわからない、○○はどうなってるんだ

連絡して♡