import praw, re

def get_reddit_post(subreddits):
    """This functions gets and display post gathered from different subreddits"""
    
    count = 1;

    #dictionary to store post id and its short url
    links = {}
    for subreddit in subreddits:
        for post in subreddit:
            #checks for news in r/dota2  
            if  (str(post.subreddit) == 'DotA2'):
                if (re.search('News',str(post.link_flair_text))):
                    print str(count)+ '\t' + str(post.subreddit) + "\t" + str(post.title)
                    links.update({count:post.short_link})
                    count += 1

            #checks for news in r/leagueoflegends        
            elif (str(post.subreddit) == "leagueoflegends"):
                criterions = []
                criterions.append(re.match('.*leagueoflegends\.com',str(post.url)))
                criterions.append(re.search('.*surrenderat20.\net', str(post.url)))

                #if the criterions are satisfied
                for criterion in criterions:
                    if criterion:
                        print str(count)+ '\t' +str(post.subreddit) + "\t" + str(post.title)
                        links.update({count:post.short_link})
                        count += 1

            #checks for news in r/virtualreality       
            elif(str(post.subreddit) == "virtualreality"):
                print str(count)+ '\t' +str(post.subreddit) + "\t" + str(post.title)
                links.update({count:post.short_link})
                count += 1

    return links
    
def fetchsubreddit(r):
    """connects to the 3 subreddit of interests and generates a list of subreddits to be parsed"""
    rdota2 = r.get_subreddit('dota2')
    rleague = r.get_subreddit('leagueoflegends')
    vr = r.get_subreddit('virtualreality')

    #get the top 10 post from the 'hot' sections of each subreddits
    dotaposts = rdota2.get_hot(limit=10)
    leagueposts = rleague.get_hot(limit= 10)
    vrpost = vr.get_hot(limit = 4)

    #and append them to a list
    subreddits = []
    subreddits.append(dotaposts)
    subreddits.append(leagueposts)
    subreddits.append(vrpost)

    #returnt the list
    return subreddits
    
if __name__== "__main__":
    r = praw.Reddit(user_agent = 'Test Script by xsaw')
    
    subreddits = fetchsubreddit(r)
    links = get_reddit_post(subreddits)

    while(1):
        num = input("\nWhich url do you want to fetch? (-1 to exit, -2 to display again) ")
        if (num == -1) :   
            break
        elif (num == -2):
            del subreddits
            subreddits = fetchsubreddit(r)
            links.update(get_reddit_post(subreddits))
        else:
            print "\nshort url: \t" + links[num] + '\n'
        

        
        
    
