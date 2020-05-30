# jsonファイルの説明

## FaceData.json

| face_list |        |      |               |      |
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

| card_list |        |               |          |           |               |                |                |                   |             |
| --------- | ------ | ------------- | -------- | --------- | ------------- | -------------- | -------------- | ----------------- | ----------- |
| id        | name   | logical_name  | cost_sun | cost_moon | victory_point | instant_effect | passive_effect | activation_effect | description |
| 0         | DEBUG  | デバッグ用のカ | 0        | 0         | 99            | NONE           | NONE           | NONE              | これはデバッ |