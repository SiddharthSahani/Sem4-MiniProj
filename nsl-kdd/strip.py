import pandas as pd

df = pd.read_csv('KDDTest+.txt')

columns = (['duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot'
,'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations'
,'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count','serror_rate'
,'srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count'
,'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate'
,'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','outcome','level'])

df.columns = columns

df.loc[df['outcome'] == "normal", "outcome"] = 'normal'
df.loc[df['outcome'] != 'normal', "outcome"] = 'attack'
df.loc[df['outcome'] == "normal", "outcome"] = 0
df.loc[df['outcome'] != 0, "outcome"] = 1

cat_cols = ['protocol_type', 'service','flag', 'land','wrong_fragment','urgent','hot', 'num_file_creations'
,'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count'
,'num_failed_logins','logged_in','level','num_compromised','root_shell']
df.drop(cat_cols, axis=1, inplace=True)
X = df.drop('outcome', axis=1)
Y = df['outcome']
Y = Y.astype('int')

X.head().to_csv('testcase.csv', index=False, header=False)
print(Y)

endcols = [i for i in columns if i not in cat_cols]
print(endcols, len(endcols))