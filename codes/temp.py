import csv
import io

new_data = '''"Toggle the 'Dark Mode' on"                 | Toggle
"Maximize the window"                       | Maximize
"Minimize the 'Settings' tab"               | Minimize
"Scroll down to the bottom of the page"     | Scroll
"Bookmark the current page"                 | Bookmark
"Zoom in on the 'Product Image'"            | Zoom
"Close the 'Product Details' pop-up"        | Close
"Refresh the page"                          | Refresh
"Scroll up to the top of the page"          | Scroll
"Bookmark the 'Help Center' page"          | Bookmark
"Open a new tab"                            | Open Tab
"Zoom out on the 'Map' section"             | Zoom
"Close the 'Terms and Conditions' window"   | Close
"Reload the page"                          | Refresh
"Scroll to the middle of the page"          | Scroll
"Bookmark the 'FAQ' page"                  | Bookmark
"Open the 'Contact Us' page"               | Open Page
"Zoom in on the 'Image Gallery'"            | Zoom
"Close the 'Chat Support' box"             | Close
"Refresh the 'Product Reviews' section"     | Refresh
"Scroll down to see more"                  | Scroll
"Bookmark the 'News' section"              | Bookmark
"Open a new 'User Profile' tab"            | Open Tab
"Zoom out on the 'Location Map'"           | Zoom
"Close the 'Privacy Policy' pop-up"         | Close
"Reload the 'User Reviews' page"           | Refresh
"Scroll up to the beginning"              | Scroll
"Bookmark the 'Services' page"            | Bookmark
"Open the 'About Us' tab"                  | Open Page
"Zoom in on the 'Main Image'"              | Zoom
"Close the 'Search Results' window"        | Close
"Refresh the 'Product Description' page"   | Refresh
"Scroll down to view more items"           | Scroll
"Bookmark the 'Customer Feedback' page"   | Bookmark
"Open a new 'Settings' tab"                | Open Tab
"Zoom out on the 'Site Map'"               | Zoom
"Close the 'Login' pop-up"                 | Close
"Reload the 'Contact Us' page"            | Refresh
"Scroll to the top of the webpage"        | Scroll
"Bookmark the 'Products' section"         | Bookmark
"Open the 'Support Center' tab"           | Open Tab
"Zoom in on the 'Product Details'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Refresh the 'FAQ' section"                | Refresh
"Scroll down to load more comments"       | Scroll
"Bookmark the 'Support Tickets' page"     | Bookmark
"Open a new 'Feedback' tab"               | Open Tab
"Zoom out on the 'Product Image'"          | Zoom
"Close the 'Product Comparison' window"   | Close
"Reload the 'Terms and Conditions' page"  | Refresh
"Scroll up to read the beginning"         | Scroll
"Bookmark the 'User Reviews' section"     | Bookmark
"Open the 'Product Description' tab"     | Open Tab
"Zoom in on the 'User Profile'"            | Zoom
"Close the 'Help Chat' box"                | Close
"Refresh the 'Privacy Policy' page"        | Refresh
"Scroll down to view more details"        | Scroll
"Bookmark the 'Contact Support' page"     | Bookmark
"Open a new 'Product Details' tab"        | Open Tab
"Zoom out on the 'Support Center'"        | Zoom
"Close the 'Order Confirmation' window"    | Close
"Reload the 'Services' page"              | Refresh
"Scroll to the top of the 'FAQ' page"     | Scroll
"Bookmark the 'Shopping Cart' page"       | Bookmark
"Open the 'My Account' tab"               | Open Tab
"Zoom in on the 'Customer Feedback'"        | Zoom
"Close the 'Chat Support' box"             | Close
"Refresh the 'User Profile' page"          | Refresh
"Scroll down to read more testimonials"    | Scroll
"Bookmark the 'About Us' page"            | Bookmark
"Open a new 'Settings' tab"                | Open Tab
"Zoom out on the 'Support Center'"        | Zoom
"Close the 'Privacy Policy' window"        | Close
"Reload the 'Contact Support' page"        | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'Home' page"                | Bookmark
"Open the 'Support Center' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Search Results' window"        | Close
"Refresh the 'FAQ' page"                   | Refresh
"Scroll down to see the full description"  | Scroll
"Bookmark the 'Help Center' page"         | Bookmark
"Open a new 'User Profile' tab"           | Open Tab
"Zoom out on the 'Product Image'"          | Zoom
"Close the 'Contact Us' window"           | Close
"Reload the 'Support Center' page"         | Refresh
"Scroll up to view more options"          | Scroll
"Bookmark the 'Pricing' page"              | Bookmark
"Open the 'Services' tab"                  | Open Tab
"Zoom in on the 'Product Details'"         | Zoom
"Close the 'Support Request' window"      | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll down to browse more products"     | Scroll
"Bookmark the 'Products' section"         | Bookmark
"Open a new 'Terms and Conditions' tab"   | Open Tab
"Zoom out on the 'Contact Us'"             | Zoom
"Close the 'Service Request' window"       | Close
"Reload the 'User Reviews' section"       | Refresh
"Scroll up to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open a new 'Contact Support' tab"       | Open Tab
"Zoom out on the 'User Reviews'"           | Zoom
"Close the 'Chat Support' box"             | Close
"Reload the 'FAQ' section"                | Refresh
"Scroll to the top of the 'About Us' page" | Scroll
"Bookmark the 'Services' page"            | Bookmark
"Open the 'Support Tickets' tab"         | Open Tab
"Zoom in on the 'Contact Us'"              | Zoom
"Close the 'Product Comparison' window"   | Close
"Refresh the 'Privacy Policy' window"      | Refresh
"Scroll down to view more testimonials"    | Scroll
"Bookmark the 'Product Description' page" | Bookmark
"Open a new 'Feedback' tab"                | Open Tab
"Zoom out on the 'User Profile'"            | Zoom
"Close the 'Help Chat' box"                | Close
"Reload the 'User Profile' page"          | Refresh
"Scroll up to read the beginning"         | Scroll
"Bookmark the 'Contact Support' page"     | Bookmark
"Open the 'Product Details' tab"         | Open Tab
"Zoom in on the 'Privacy Policy'"          | Zoom
"Close the 'Order Confirmation' window"    | Close
"Refresh the 'Services' page"              | Refresh
"Scroll to the top of the 'Support Center'" | Scroll
"Bookmark the 'Home' page"                | Bookmark
"Open the 'Checkout' tab"                  | Open Tab
"Zoom out on the 'Product Comparison'"      | Zoom
"Close the 'Search Results' window"        | Close
"Reload the 'Service Request' page"        | Refresh
"Scroll down to see the full description"  | Scroll
"Bookmark the 'About Us' page"            | Bookmark
"Open the 'Pricing' tab"                  | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Contact Us' window"           | Close
"Refresh the 'Contact Support' page"      | Refresh
"Scroll up to view more options"          | Scroll
"Bookmark the 'Services' page"            | Bookmark
"Open the 'FAQ' tab"                      | Open Tab
"Zoom out on the 'Product Details'"         | Zoom
"Close the 'Support Request' window"      | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more details"        | Scroll
"Bookmark the 'Service Request' page"     | Bookmark
"Open the 'User Profile' tab"             | Open Tab
"Zoom in on the 'Product Image'"            | Zoom
"Close the 'Feedback Form' window"         | Close
"Refresh the 'FAQ' page"                   | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Reviews' section"     | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Chat Support' box"             | Close
"Reload the 'Privacy Policy' window"        | Refresh
"Scroll down to browse more products"       | Scroll
"Bookmark the 'Support Center' page"       | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll up to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh
"Scroll to the top of the 'Services' page" | Scroll
"Bookmark the 'User Profile' tab"         | Bookmark
"Open the 'Customer Feedback' tab"         | Open Tab
"Zoom out on the 'Service Request'"         | Zoom
"Close the 'Feedback Form' window"         | Close
"Reload the 'Service Request' page"      | Refresh
"Scroll down to view more options"        | Scroll
"Bookmark the 'Support Center' page"     | Bookmark
"Open the 'Contact Support' tab"           | Open Tab
"Zoom in on the 'Service Request'"         | Zoom
"Close the 'Service Request' window"       | Close
"Refresh the 'Service Request' page"      | Refresh'''


# Split the new data into rows
new_data = [line.split('|') for line in new_data.split('\n')]

# Remove any leading/trailing spaces
new_data = [[cell.strip() for cell in row] for row in new_data]

# Define the existing CSV file
csv_file = "commands_and_actions.csv"

# Read the existing data from the CSV file
existing_data = []
try:
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            existing_data.append(row)
except FileNotFoundError:
    # The file does not exist, create it with headers
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Command", "Action"])

# Append the new data to the existing data
existing_data.extend(new_data)

# Write the combined data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    for row in existing_data:
        writer.writerow(row)

print(f"Data has been appended to {csv_file}.")
