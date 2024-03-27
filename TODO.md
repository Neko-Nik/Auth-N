# Required features:

- [ ] Register a new user
- [ ] Login
- [ ] Logout
- [ ] Delete user
- [ ] Update user information
- [ ] Get user information
- [ ] User should be of a specific role
    - [ ] Apex Team: Internal Team who has access to all the features
    - [ ] Alliance Team: Our partners that can add / create / delete super admins under them
    - [ ] Super Admin: Can add / create / delete Admins and Users under them
    - [ ] Admin: Has some level of restriction to the super admin features (Highly customizable)
    - [ ] Standard Users: Will have access to the features that are assigned to them by the super admin or admin
- [ ] Password policy should be enforced
- [ ] User should be able to reset password
- [ ] User should be able to change password
- [ ] User should be able to change email
- [ ] User should be able to change phone number
- [ ] User should be able to change profile picture
- [ ] User should be able to change profile information
- [ ] JWT Token should be used for authentication
- [ ] JWT Token should be refreshed after a certain period of time
- [ ] Revoking JWT Token should be possible
- [ ] API Key based authentication for the Machine to Machine communication
- [ ] User should be able to see the list of users under them (if they have any)
- [ ] IP based restriction for the user
- [ ] Cross-Site Request Forgery (CSRF) protection
- [ ] Cross-Origin Resource Sharing (CORS) protection
- [ ] Passwordless login using OTP from email or SMS
- [ ] 2FA using TOTP or HOTP or U2F or WebAuthn or SMS or Email
- [ ] User should be able to see the list of devices / sessions that are logged in
- [ ] User should be able to logout from desired devices or all devices at once, nothing but revoking the JWT Token
- [ ] Account lockout after a certain number of failed login attempts
- [ ] Audit logs for the user actions
- [ ] Multi tenancy support (Single DB, Multiple Schema or Multiple DB, Multiple Schema)
- [ ] User should be able to see the list of roles that are available in the system
- [ ] User should be able to see the list of permissions that are available in the system


# Database Schema

The database (PostgreSQL) schema for the user management system will consist of the following tables:

## Tables:

1. **Users:**
   - user_id (Primary Key)
   - username
   - password_hash
   - email
   - phone_number
   - profile_picture_url
   - last_login
   - is_active
   - is_locked
   - lockout_time
   - created_at
   - updated_at
   - password_last_changed

2. **Roles:**
   - role_id (Primary Key)
   - role_name

3. **Permissions:**
   - permission_id (Primary Key)
   - permission_name

4. **User_Roles:**
   - user_id (Foreign Key to Users)
   - role_id (Foreign Key to Roles)

5. **Role_Permissions:**
   - role_id (Foreign Key to Roles)
   - permission_id (Foreign Key to Permissions)

6. **Login_Attempts:**
   - attempt_id (Primary Key)
   - user_id (Foreign Key to Users)
   - attempt_time
   - success (Boolean)
   - ip_address

7. **Audit_Logs:**
   - log_id (Primary Key)
   - user_id (Foreign Key to Users)
   - action
   - timestamp
   - details

8. **Sessions:**
   - session_id (Primary Key)
   - user_id (Foreign Key to Users)
   - device_info
   - login_time
   - last_activity_time
   - is_active

9. **JWT_Tokens:**
   - token_id (Primary Key)
   - user_id (Foreign Key to Users)
   - token
   - expiration_time

10. **API_Keys:**
    - key_id (Primary Key)
    - user_id (Foreign Key to Users)
    - key
    - created_at
    - last_used_at

11. **Password_Reset_Tokens:**
    - token_id (Primary Key)
    - user_id (Foreign Key to Users)
    - token
    - expiration_time

12. **IP_Restrictions:**
    - restriction_id (Primary Key)
    - user_id (Foreign Key to Users)
    - ip_address

13. **CSRF_Tokens:**
    - token_id (Primary Key)
    - user_id (Foreign Key to Users)
    - token
    - expiration_time

14. **OTP_Tokens:**
    - token_id (Primary Key)
    - user_id (Foreign Key to Users)
    - token
    - expiration_time

15. **Device_List:**
    - device_id (Primary Key)
    - user_id (Foreign Key to Users)
    - device_info
    - last_login

16. **Account_Lockout_Logs:**
    - log_id (Primary Key)
    - user_id (Foreign Key to Users)
    - attempt_time
    - ip_address

### Relationships:

- **Users** and **Roles** have a many-to-many relationship through the **User_Roles** table
- **Roles** and **Permissions** also have a many-to-many relationship through the **Role_Permissions** table
- **Users** are related to **Login_Attempts**, **Audit_Logs**, **Sessions**, **JWT_Tokens**, **API_Keys**, **Password_Reset_Tokens**, **IP_Restrictions**, **CSRF_Tokens**, **OTP_Tokens**, **Device_List**, and **Account_Lockout_Logs** through foreign key relationships
- **Roles** are assigned to users through the **User_Roles** table
- **Permissions** are associated with roles via the **Role_Permissions** table

### Complex Features:

- **Password Policy:** Not represented directly in the schema, but enforced in the application logic
- **JWT Token:** Stored in the **JWT_Tokens** table
- **JWT Token Refresh:** Expiration time is handled in the **JWT_Tokens** table
- **Revoking JWT Token:** Deleting records from the **JWT_Tokens** table
- **API Key Authentication:** Stored in the **API_Keys** table
- **IP-based Restriction:** Stored in the **IP_Restrictions** table
- **CSRF Protection:** Handled in the application logic, CSRF tokens stored in the **CSRF_Tokens** table
- **Passwordless Login:** OTP tokens stored in the **OTP_Tokens** table
- **2FA:** OTP tokens stored in the **OTP_Tokens** table
- **List of Devices/Sessions:** Stored in the **Device_List** table
- **Logout from Devices:** Removing records from the **Device_List** table
- **Account Lockout:** Account lockout logs stored in the **Account_Lockout_Logs** table
- **Audit Logs:** Stored in the **Audit_Logs** table
- **Multi-Tenancy:** Not represented in the schema, but can be implemented using a multi-tenant architecture
