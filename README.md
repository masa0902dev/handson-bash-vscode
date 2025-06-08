# コード例 (研究室のためのターミナルとエディタの環境構築: bash, VScode)

[研究室のためのターミナルとエディタの開発環境構築: bash, VScode](https://zenn.dev/masa0902dev/articles/editor-terminal-vscode-git-bash)

こちらの記事内で書いた，簡単な粒子シミュレーションのコードです．  
「main.pyに全てのコードを書いて1万行とかのファイルを作らないでね」「処理を細分化して関数にし, その関数たちを使って処理フローを作ってね」という意図のコード例になっています．

※シミュレーション自体に意味はありません．

## 実行の手順
python 3.13 で動作角をしました．

1. `pip install -r requirements.txt`でnumpy等のパッケージをインストール
2. `python main.py`でシミュレーションを実行
3. GIFが生成されるので, /data/output/simulation.gif を見てみる
