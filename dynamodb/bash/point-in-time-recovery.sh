# /bin/sh
TABLE_NAME=wx_data
# if table is ACTIVE, point-in-time recovery (point-in-time リカバリとは、特定の時点までのデータ変更のリカバリのことです。 一般に、この種類のリカバリは、サーバーをバックアップが行われた時点の状態にする完全バックアップのリストア後に実行されます)
aws dynamodb update-continuous-backups --table-name $TABLE_NAME --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true 
