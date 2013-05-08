DataPad user management
=====

DataPad is going to have users in groups
with credentials for third-party services.
We need some way of managing that. The
present repository presents a story about
what we'll need to represent. Then it
discusses how to implement it with a few
different services.

## Services
Here are the services I looked at. This is
a pretty broad range, and it includes things
that are totally off the mark; I included
these so that we can quickly remember later
not to use them.

* http://singly.com/
* http://janrain.com/products/
* http://www.gigya.com/user-management/registration-as-a-service/
* http://aws.amazon.com/iam/
* https://www.dailycred.com/
* https://stormpath.com/

## Story
Thomas and Tomasina work at a marketing firm that is consulting for a tank
engine company. They are collaborating on a data analysis about the market
for tank engines, and they are using DataPad. They want to figure out which
cities they should tarket their marketing in.

They pull data from a few sources.

1. Internal spreadsheets
2. Stock market, via Yahoo
3. Twitter
4. Large private datasets stored on S3
5. Google Analytics

The last three of these services require special credentials (API keys).

Now let's focus on user accounts. This is not the only project that Thomas
and Tomasina work on, they don't always collaborate, and it's nice to see
who has done what. Thus, they want their own accounts, each with access to
this project.

They have a company-wide Twitter API key. For S3, they prefer to use separate
accounts for each project for security reasons. They're using the tank engine
company's Google Analytics credentials.

Thomas or Tomasina will specify these credentials, and it's fine, and perhaps
desirable, if the other of them can see the credential once it has been set.

They want to be able to share a read-only version of the analysis quite
publically within the two companies. In order that this analysis be safe to
share publically, people viewing version of the analysis should not be able
to see the third-party credentials.

## Architecture ideas
It seems like following GitHub's model would work pretty well.

People log in with their personal user account. Each account can be associated
with any number of organizations. Projects belong to either a user or an
organization. Credentials belong to a user, organization or project.

Handling collaborators on a personal project is a bit inelegant to me. It also
makes things more complicated to use. Maybe multi-person projects automatically
morph into organizations....

I'd like to think more about this, but for now, I'm going to try implementing this
architecture with the aforementioned services.
