# コード例 (研究室のためのターミナル, エディタの開発構築: bash, VScode)

[研究室のためのターミナル, エディタの開発環境: bash, VScode](https://zenn.dev/masa0902dev/articles/editor-terminal-vscode-git-bash)

上記の記事で触れた，簡単な粒子シミュレーションのコードです．  
「main.pyに全てのコードを書いて1万行とかのファイルを作らないでね」「処理を細分化して関数にし, その関数たちを使って処理フローを作ってね」という意図のコード例になっています．

※シミュレーション自体に意味はありません．

## 実行の手順
python 3.13 で動作確認をしました．

1. `pip install -r requirements.txt`でnumpy等のパッケージをインストール
2. `python main.py`でシミュレーションを実行
3. GIFが生成されるので, /data/output/simulation.gif を見てみる
