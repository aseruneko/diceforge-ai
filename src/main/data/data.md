# jsonファイルの説明

## FaceData.json

| card_list |        |      |               |      |
| --------- | ------ | ---- | ------------- | ---- |
| id        | name   | tag  | val           | cost |
| 0         | DEBUG  | +    |  *辞書のリスト | 0    |
| 1         | GOLD_1 | gold | 1              | 0   |
| 2         | VP_2   | vp   | 2             | 0    |
| ...       | ...    | ...  | ...           | ...  |

- 辞書のリストの例

```
{
    "id" : 8,
    "name" : "+_SUN_1_VP_1",
    "tag" : "+",
    "val" : [
        {
            "tag" : "sun",
            "val" : 1
        },
        {
            "tag" : "vp",
            "val" : 1
        }
    ],
    "cost" : 4
}
```

## CardData.json

- 作成予定（未実装）