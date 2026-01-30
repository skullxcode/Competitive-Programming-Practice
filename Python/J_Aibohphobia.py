t = int(input())
for _ in range(t):
    s = input()
    if len(s)==1:
        print("YES")
        print(s)
    else:
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0)+1
        sorted_items = sorted(freq.items(), key=lambda item: item[1])
        freq_desc = dict(sorted_items)
        keys_list = list(freq_desc.keys())
        n = len(keys_list)
        if freq_desc[keys_list[0]]==1:
            ans = ""
            for i in range(0,n):
                ans+=keys_list[i]*freq_desc[keys_list[i]]
            print("YES")
            print(ans)
        elif len(keys_list)>2:
            ans = []
            for i in keys_list:
                ans.append(i)
                freq_desc[i]-=1
            for i in keys_list:
                ans.append(i*freq_desc[i])
            ans = "".join(ans)
            if ans==ans[::-1]:
                print("NO")
            else:
                print("YES")        
                print(ans)
        else:
            print("NO")
        
            # i = 0
            # cnt = 0
            # cont = 0
            # while cnt<len(s):
            #     if freq_desc[keys_list[i]]>0:
            #         ans.append(keys_list[i])
            #         freq_desc[keys_list[i]]-=1
            #         cnt+=1
            #     if i==n-1 and freq_desc[keys_list[i]]==0:
            #         break
            #     if freq_desc[keys_list[i]]==0:
            #         cont=i+1
            #     if keys_list[i]==keys_list[-1]:
            #         i = cont
            #         continue
            #     i+=1
        
        
        # elif freq_desc[keys_list[0]]==2 and len(keys_list)>2:
        #     ans = keys_list[0]
        #     for i in range(1,n):
        #         ans+=keys_list[i]*freq_desc[keys_list[i]]
        #     ans+= keys_list[0]
        #     print("YES")
        #     print(ans)
        # else:
        #     print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # f = True
        # g = True
        # li = []
        # for i in s:
        #     li.append(i)
        # li.sort()
        # s = "".join(li)
        # li.reverse()
        # k = "".join(li)
        # if s[0]==s[1]:
        #         s+=s[1]
        #         s=s[1::]
        # if s==s[::-1] or s.count(s[0])>2:
        #     f = False
        #     if k[0]==k[1]:
        #         k+=k[1]
        #         k=k[1::]
        #     if k==k[::-1] or k.count(k[0])>2:
        #         g = False
        
        # if f==False:
        #     if g==False:
        #         print("NO")
        #     else:
        #         print("YES")
        #         print(k)
        # else:
        #     print("YES")
        #     print(s)