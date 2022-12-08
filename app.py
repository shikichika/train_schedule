import streamlit as st
import datetime
from pytz import timezone
import jpholiday



dt_now = datetime.datetime.now(timezone('Asia/Tokyo'))
now_h = dt_now.hour
result = jpholiday.is_holiday(dt_now)

working_days_train = {6:[47], 7:[7,27, 39, 59], 8:[10, 20, 30, 46, 57], 9:[14, 28, 43, 58], 10:[13, 28, 43, 58], 11:[13, 28, 43, 58],12:[13, 28, 43, 58], 13:[13, 28, 43, 58], 14:[13, 28, 43, 58], 15:[13, 28, 43, 58], 16:[13, 27, 42, 57], 17:[12, 27, 42, 57], 18:[12, 27, 42, 57], 19:[12, 27, 42, 57], 20:[12, 27, 42, 57], 21:[12, 27], 22:[2, 22, 42], 23:[2, 22, 42]}
weekend_days_train = {7:[27, 42, 51, 57], 8:[12, 27, 42, 57], 9:[13, 28, 43, 58], 10:[13, 21, 28, 43, 58], 11:[13, 21, 28, 43, 58], 12:[13, 28, 43, 58], 13:[13, 28, 43, 58], 14:[13, 28, 43, 58], 15:[13, 28, 43, 58], 16:[13, 27, 42, 57], 17:[12, 27, 42, 57], 18:[12, 27, 42, 57], 19:[12, 27, 42, 57], 20:[12, 27, 42, 57], 21:[2, 22, 42], 22:[2, 22, 42], 23:[2, 22, 42]}


if result == True or (dt_now.weekday() == 5 or dt_now.weekday() == 6):
    st.write("Weekends or Holiday")
    st.write("Today: "+ str(dt_now.year)+"/"+str(dt_now.month)+"/"+str(dt_now.day))
    if now_h in [0, 1, 2, 3, 4, 5, 6]:
        st.write("Now train")
    else:
        now_m = dt_now.minute
        next_train_h = now_h
        next_train_m = 100
        after_next_train_h = now_h
        after_next_train_m = 100
        for i in range(len(weekend_days_train[now_h])):
            if weekend_days_train[now_h][i] > now_m:
                next_train_m = weekend_days_train[now_h][i]
                if i <= len(weekend_days_train[now_h])-2:
                    after_next_train_m = weekend_days_train[now_h][i+1]
                else:
                    after_next_train_h = now_h+1
                    try:
                        after_next_train_m = weekend_days_train[now_h+1][0]
                    except:
                        after_next_train_h = now_h
                        after_next_train_m = next_train_m
                    
                break

        if next_train_m == 100:
            next_train_h = now_h+1
            next_train_m = weekend_days_train[now_h+1][0]
            if len(weekend_days_train[now_h+1]) > 1:
                after_next_train_h = now_h + 1
                after_next_train_m= weekend_days_train[now_h+1][1]
            elif len(weekend_days_train[now_h+1]) > 1:
                after_next_train_h = now_h + 2
                after_next_train_m= weekend_days_train[now_h+2][0]
            

            

        dt1 = datetime.datetime(year= dt_now.year, month=dt_now.month, day=dt_now.day, hour=dt_now.hour, minute=dt_now.minute)
        dt2 = datetime.datetime(year= dt_now.year, month=dt_now.month, day=dt_now.day, hour=next_train_h, minute=next_train_m)

else:
    st.write("Working day")
    st.write("Today: "+ str(dt_now.year)+"/"+str(dt_now.month)+"/"+str(dt_now.day))
    
    if now_h in [0, 1, 2, 3, 4, 5]:
        st.write("Now train")
    else:
        now_m = dt_now.minute
        next_train_h = now_h
        next_train_m = 100
        after_next_train_h = now_h
        after_next_train_m = 100
        for i in range(len(working_days_train[now_h])):
            if working_days_train[now_h][i] > now_m:
                next_train_m = working_days_train[now_h][i]
                if i <= len(working_days_train[now_h])-2:
                    after_next_train_m = working_days_train[now_h][i+1]
                else:
                    after_next_train_h = now_h+1
                    try:
                        after_next_train_m = working_days_train[now_h+1][0]
                    except:
                        after_next_train_h = now_h
                        after_next_train_m = next_train_m

                break

        if next_train_m == 100:
            next_train_h = now_h+1
            next_train_m = working_days_train[now_h+1][0]
            if len(working_days_train[now_h+1]) > 1:
                after_next_train_h = now_h + 1
                after_next_train_m = working_days_train[now_h+1][1]
            elif len(working_days_train[now_h+1]) > 1:
                try:
                    after_next_train_h = now_h + 2
                    after_next_train_m = working_days_train[now_h+2][0]
                except:
                    after_next_train_h = now_h+1
                    after_next_train_m = next_train_m

            

dt1 = datetime.datetime(year= dt_now.year, month=dt_now.month, day=dt_now.day, hour=dt_now.hour, minute=dt_now.minute)
dt2 = datetime.datetime(year= dt_now.year, month=dt_now.month, day=dt_now.day, hour=next_train_h, minute=next_train_m)

st.title("The next special rapid train is " + str(next_train_h) +":"+ str(next_train_m))
st.header(str(int(((dt2-dt1).seconds)/60))+" min left" )
st.header("The special rapid train after the next train "+str(after_next_train_h)+":"+str(after_next_train_m))

