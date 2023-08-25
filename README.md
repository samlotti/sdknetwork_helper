# SKAdNetworkIdentifier list helper

Simple tool to cleanup the SKAdNetworkIdentifier from the info.plist.

# Problem statement:

Over time my list of sdk networks has grown to an unmanagable number of entries in the info.plist. This was due to using different advertisers or just using a mediation.

## Case Sensitivity

Does case matter? Some advertisers had mixed cases entries. Here's a thread where the conclusion is that when need to be lowercase [https://developer.apple.com/forums/thread/663032].

## Duplicate entries

In my list I have many duplicates, some with difference cases. Each advertiser provides a list of network identifiers and the can contains the same entries causing duplicates. These list of entries change over time and they tell you to update your list (when to do this?).

Here's a page for admob (admoblist)[https://developers.google.com/admob/ios/ios14#skadnetwork]

Don't forget that these lists can change and you need to update the plist with the changes. How do you know what needs to be added / removed?

# Solution

A bit of a hack maybe. In my case I keep a file with the copy / paste of the advertisers list.

Whenever I update the app I go to the advertisers and append to the my current list.

Then run this python script that will convert to lowercase, dedup the entries and same into the output.txt file.

Open the info.plist, delete the section between:

```
	<key>SKAdNetworkItems</key>
	<array>
```

and

```
	</array>
```

Then paste the output between the tags.

Hope this helps others.

```
  python cleanup.py
```
