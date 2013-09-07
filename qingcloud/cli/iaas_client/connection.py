"""
Created on 2012-6-26

@author: yunify
"""

from qingcloud.cli.conn.connection import HttpConnection
from constants import ACTION_DESCRIBE_IMAGES, ACTION_DESCRIBE_INSTANCES, \
                      ACTION_RUN_INSTANCES, ACTION_STOP_INSTANCES, \
                      ACTION_TERMINATE_INSTANCES, ACTION_CREATE_VOLUMES, \
                      ACTION_DESCRIBE_VOLUMES, ACTION_DELETE_VOLUMES, \
                      ACTION_ATTACH_VOLUMES, ACTION_DETACH_VOLUMES, \
                      ACTION_CAPTURE_INSTANCE, ACTION_DELETE_IMAGES, \
                      ACTION_DELETE_BROKERS, ACTION_CREATE_BROKERS, \
                      ACTION_DESCRIBE_KEY_PAIRS, ACTION_DESCRIBE_INSTANCE_TYPES, \
                      ACTION_DESCRIBE_ZONES, ACTION_MODIFY_IMAGE_ATTRIBUTES, \
                      ACTION_MODIFY_INSTANCE_ATTRIBUTES, ACTION_MODIFY_VOLUME_ATTRIBUTES, \
                      ACTION_DESCRIBE_EIPS, ACTION_ATTACH_KEY_PAIRS, ACTION_DETACH_KEY_PAIRS, \
                      ACTION_CREATE_KEY_PAIR, ACTION_DELETE_KEY_PAIRS, \
                      ACTION_DESCRIBE_JOBS, ACTION_DESCRIBE_ACCESS_KEYS, \
                      ACTION_DESCRIBE_SECURITY_GROUPS, ACTION_CREATE_SECURITY_GROUP, \
                      ACTION_MODIFY_SECURITY_GROUP_ATTRIBUTES, ACTION_APPLY_SECURITY_GROUP, \
                      ACTION_DELETE_SECURITY_GROUPS, \
                      ACTION_DESCRIBE_VXNETS, ACTION_CREATE_VXNETS, ACTION_DELETE_VXNETS, \
                      ACTION_MODIFY_KEYPAIR_ATTRIBUTES, ACTION_MODIFY_VXNET_ATTRIBUTES, \
                      ACTION_CREATE_ACCESS_KEY, ACTION_DELETE_ACCESS_KEYS, ACTION_MODIFY_USER_ATTRIBUTES, \
                      ACTION_UPDATE_GRAPHICS_PASSWD, ACTION_GET_MONITOR, ACTION_CHANGE_PASSWORD, \
                      ACTION_SEND_CONFIRM_EMAIL, ACTION_GET_PRIVATE_KEY, ACTION_RESTART_INSTANCES, \
                      ACTION_GET_BALANCE, ACTION_LEASE, ACTION_GET_LEASE_INFO, \
                      ACTION_GET_PRICE, ACTION_GET_CHARGE_RECORDS, ACTION_JOIN_VXNET, \
                      ACTION_LEAVE_VXNET, ACTION_GET_RECHARGE_RECORDS, \
                      ACTION_DESCRIBE_TICKETS, ACTION_OPEN_TICKET, ACTION_CLOSE_TICKETS, ACTION_ADD_TICKET_REPLY, \
                      ACTION_GET_CHARGE_RESOURCES, ACTION_GET_CHARGE_SUMMARY, ACTION_SEND_EMAIL_VERI_CODE, \
                      ACTION_CHANGE_EMAIL, ACTION_GET_RESOURCE_SUMMARY, ACTION_DESCRIBE_TICKET_REPLIES, \
                      ACTION_ASSOCIATE_EIP, ACTION_DISSOCIATE_EIPS, ACTION_ALLOCATE_EIPS, ACTION_RELEASE_EIPS, \
                      ACTION_MODIFY_EIP_ATTRIBUTES, ACTION_RESIZE_INSTANCES, ACTION_RESIZE_VOLUMES, \
                      ACTION_CHANGE_EIPS_BANDWIDTH, ACTION_DESCRIBE_SECURITY_GROUP_RULES, ACTION_ADD_SECURITY_GROUP_RULES, \
                      ACTION_DELETE_SECURITY_GROUP_RULES, ACTION_MODIFY_SECURITY_GROUP_RULE_ATTRIBUTES, \
                      ACTION_MODIFY_ACCESS_KEY_ATTRIBUTES, ACTION_RESET_INSTANCES, ACTION_START_INSTANCES, \
                      ACTION_CREATE_ROUTERS, ACTION_UPDATE_ROUTERS, ACTION_DELETE_ROUTERS, \
                      ACTION_DESCRIBE_ROUTERS, ACTION_MODIFY_ROUTER_ATTRIBUTES, ACTION_DESCRIBE_ROUTER_STATICS, \
                      ACTION_ADD_ROUTER_STATICS, ACTION_DELETE_ROUTER_STATICS, ACTION_DESCRIBE_VXNET_INSTANCES, \
                      ACTION_JOIN_ROUTER, ACTION_LEAVE_ROUTER, ACTION_DESCRIBE_ROUTER_VXNETS, ACTION_GET_VPN_CERTS, \
                      ACTION_POWEROFF_ROUTERS, ACTION_POWERON_ROUTERS, ACTION_RESIZE_ROUTERS


class APIConnection(HttpConnection):
    """
    Public connection to qingcloud service
    """

    def _build_request(self, body):
        """ build request """
        request = {}
        for k in body:
            request[k] = body[k]

        return request

    def send_request(self, action, body, url = '/iaas/', verb = 'GET'):
        """ send request """
        request = self._build_request(body)
        request['action'] = action
        if 'zone' not in request:
            request['zone'] = self.zone

        return self.send(url, request, verb)

    def describe_images(self, images = None,
                              platform = None,
                              architecture = None,
                              os_family = None,
                              hypervisor = None,
                              status = None,
                              transition_status = None,
                              visibility = None,
                              provider = "self",
                              verbose = 0,
                              image_name = None,
                              offset = None,
                              limit = None,
                              **params):
        """ Action:DescribeImages
            @param images: An array including IDs of the images you want to list.
                          No ID specified means list all.
            @param platform: What kind of bundled OS of the images you want to list.
                            Linux, Windows, OpenSolaris. No platform specified means list all.
            @param architecture: x86_64, i386.
            @param hypervisor: xen, kvm.
            @param status: Status of the image. Valid values include pending, available, deleted.
            @param transition_status: Status of the image in transition, including creating, deleting.
            @param visibility: Who can see and use this image. Valid values include public, private, shared.
            @param provider: who provide this image, self, system or image-shop.
            @param verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
            @param image_name: the name of the image. Support partial match.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_IMAGES
        body = {}
        if images:
            body['images'] = images
        if platform:
            body['platform'] = platform
        if architecture:
            body['architecture'] = architecture
        if os_family:
            body['os_family'] = os_family
        if hypervisor:
            body['hypervisor'] = hypervisor
        if status:
            body['status'] = status
        if transition_status:
            body['transition_status'] = transition_status
        if visibility:
            body['visibility'] = visibility
        if provider:
            body['provider'] = provider
        if verbose:
            body['verbose'] = verbose
        if image_name:
            body['image_name'] = image_name
        if offset:
            body['offset'] = offset
        if limit :
            body['limit'] = limit

        return self.send_request(action, body)

    def capture_instance(self, instance,
                         image_name = "",
                         **params):
        """ Action: CaptureInstance
            @param instance: ID of the instance you want to capture.
            @param image_name: A short name of the image.
        """
        action = ACTION_CAPTURE_INSTANCE
        body = {}
        if instance:
            body['instance'] = instance
        if image_name:
            body['image_name'] = image_name

        return self.send_request(action, body)

    def delete_images(self, images,
                              **params):
        """ Action: ACTION_DELETE_IMAGES
            @param images: ID of the images you want to delete.
        """
        action = ACTION_DELETE_IMAGES
        body = {}
        if images:
            body['images'] = images

        return self.send_request(action, body)

    def modify_image_attributes(self, image,
                                      image_name = None,
                                      description = None,
                                      **params):
        """ @param image: the ID of image whose attributes you want to modify.
            @param image_name: Name of the image. It's a short name for the image
                               that more meaningful than image id.
            @param description: The detailed description of the resource.
        """
        action = ACTION_MODIFY_IMAGE_ATTRIBUTES
        body = {}
        if image:
            body['image'] = image
        if image_name is not None:
            body['image_name'] = image_name
        if description is not None:
            body['description'] = description

        return self.send_request(action, body)

    def describe_instances(self, instances = None,
                                 image_id = None,
                                 instance_type = None,
                                 graphics_protocol = None,
                                 status = None,
                                 transition_status = None,
                                 instance_name = None,
                                 verbose = 0,
                                 offset = None,
                                 limit = None,
                                 **params):
        """ Action:DescribeInstances
            @param instances : the array of IDs of instances
            @param image_id : ID of the image which is used to launch this instance.
            @param instance_type: The instance type.
            @param graphics_protocol: The graphics protocol, spice is supported.
            @param status : Status of the instance, including pending, running, stopped, terminated.
            @param transition_status: Status of the instance in transition, including creating, starting, stopping, terminating.
            @param verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
            @param instance_name: the name of the instance. Support partial match.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_INSTANCES
        body = {}
        if instances:
            body['instances'] = instances
        if image_id:
            body['image_id'] = image_id
        if instance_type:
            body['instance_type'] = instance_type
        if graphics_protocol:
            body['graphics_protocol'] = graphics_protocol
        if status:
            body['status'] = status
        if transition_status:
            body['transition_status'] = transition_status
        if instance_name:
            body['instance_name'] = instance_name
        if verbose:
            body['verbose'] = verbose
        if offset:
            body['offset'] = offset
        if limit :
            body['limit'] = limit

        return self.send_request(action, body)

    def run_instances(self, image_id,
                            instance_type = None,
                            cpu = None,
                            memory = None,
                            count = 1,
                            instance_name = "",
                            vxnets = None,
                            security_group = None,
                            login_mode = None,
                            login_keypair = None,
                            login_passwd = None,
                              **params):
        """ Action:RunInstance
            @param image_id : ID of the image you want to use, "img-12345"
            @param instance_type: What kind of instance you want to launch. "micro", "small", "medium", "large".
            @param cpu: cpu core number.
            @param memory: memory size in MB.
            @param instance_name: a meaningful short name of instance.
            @param count : The number of instances to launch, default 1.
            @param instance_type : e.g., "micro", "small", "medium", "large".
            @param vxnets : The IDs of vxnets the instance will join.
            @param security_group: The ID of security group that will apply to instance.
            @param login_mode: ssh login mode, "keypair" or "passwd"
            @param login_keypair: login keypair id
            @param login_passwd: login passwd
        """
        action = ACTION_RUN_INSTANCES
        body = {}
        body['image_id'] = image_id
        if instance_type:
            body['instance_type'] = instance_type
        if cpu:
            body['cpu'] = cpu
        if memory:
            body['memory'] = memory
        if count:
            body['count'] = count
        if instance_name:
            body['instance_name'] = instance_name
        if vxnets:
            body['vxnets'] = vxnets
        if security_group:
            body['security_group'] = security_group
        if login_mode:
            body['login_mode'] = login_mode
        if login_keypair:
            body['login_keypair'] = login_keypair
        if login_passwd:
            body['login_passwd'] = login_passwd

        return self.send_request(action, body)

    def terminate_instances(self, instances,
                              **params):
        """ Action:TerminateInstances
            @param instances : An array including IDs of the instances you want to terminate.
        """

        action = ACTION_TERMINATE_INSTANCES
        body = {}
        body["instances"] = instances

        return self.send_request(action, body)

    def stop_instances(self, instances,
                             force=0,
                             **params):
        """ Action:StopInstances
            @param instances : An array including IDs of the instances you want to stop.
            @param force: 0 for gracefully shutdown and 1 for forcibly shutdown.
        """

        action = ACTION_STOP_INSTANCES
        body = {}
        body["instances"] = instances
        force = 1 if force != 0 else 0
        body["force"] = force

        return self.send_request(action, body)

    def restart_instances(self, instances,
                              **params):
        """ Action:RestartInstances
            @param instances : An array including IDs of the instances you want to restart.
        """

        action = ACTION_RESTART_INSTANCES
        body = {}
        body["instances"] = instances

        return self.send_request(action, body)

    def start_instances(self, instances,
                              **params):
        """ Action:StartInstances
            @param instances : An array including IDs of the instances you want to start.
        """

        action = ACTION_START_INSTANCES
        body = {}
        body["instances"] = instances

        return self.send_request(action, body)

    def reset_instances(self, instances,
                              **params):
        """ Action:ResetInstances
            @param instances : An array including IDs of the instances you want to reset.
        """

        action = ACTION_RESET_INSTANCES
        body = {}
        body["instances"] = instances

        return self.send_request(action, body)

    def resize_instances(self,
                         instances,
                         instance_type=None,
                         cpu=None,
                         memory=None,
                         **params):
        """ Action:ResizeInstances
            @param instances: the IDs of the instances you want to resize.
            @param instance_type: What kind of instance you want to launch.
            @param cpu: cpu core number.
            @param memory: memory size in MB.
        """
        # build request
        action = ACTION_RESIZE_INSTANCES
        body = {}
        body['instances'] = instances
        if instance_type is not None:
            body['instance_type'] = instance_type
        if cpu is not None:
            body['cpu'] = cpu
        if memory is not None:
            body['memory'] = memory

        return self.send_request(action, body)

    def modify_instance_attributes(self, instance,
                                         instance_name = None,
                                         description = None,
                                         **params):
        """ @param instance:  the ID of instance whose attributes you want to modify.
            @param instance_name: Name of the instance. It's a short name for the instance
                                  that more meaningful than instance id.
            @param description: The detailed description of the resource.
        """
        action = ACTION_MODIFY_INSTANCE_ATTRIBUTES
        body = {}
        if instance:
            body['instance'] = instance
        if instance_name is not None:
            body['instance_name'] = instance_name
        if description is not None:
            body['description'] = description

        return self.send_request(action, body)

    def create_brokers(self, instances,
                              **params):
        """ Action: ACTION_CREATE_BROKERS
            @param instances: IDs of the instances you want to create broker for.
        """
        action = ACTION_CREATE_BROKERS
        body = {}
        if instances:
            body['instances'] = instances

        return self.send_request(action, body)

    def delete_brokers(self, instances,
                              **params):
        """ Action: ACTION_DELETE_BROKERS
            @param instances: IDs of the instances whose broker you want to remove.
        """
        action = ACTION_DELETE_BROKERS
        body = {}
        if instances:
            body['instances'] = instances

        return self.send_request(action, body)

    def update_graphic_passwd(self, instances, **params):
        """
            @param instances: the IDs of instances you want to update their graphic passwords.
        """
        action = ACTION_UPDATE_GRAPHICS_PASSWD
        body = {}
        if instances:
            body['instances'] = instances

        return self.send_request(action, body)

    def get_monitor(self, resource,
                    meters,
                    step,
                    start_time,
                    end_time,
                    **params):
        """
            @param resource: the ID of resource whose monitoring data you want to get.
            @param meters: a list of metering types you want to get.
                           e.g. "cpu", "disk_rd-<volume id>", "disk_wr-<volume id>",
                                "if_rx-<mac address>", "if_tx-<mac address>"
            @param step: the metering time step. e.g. "1m", "5m", "15m", "30m",
                         "1h", "2h", "1d"
            @param start_time: the starting time stamp.
            @param end_time: the ending time stamp.
        """
        action = ACTION_GET_MONITOR
        body = {}
        if resource:
            body['resource'] = resource
        if meters:
            body['meters'] = meters
        if step:
            body['step'] = step
        if start_time:
            body['start_time'] = start_time
        if end_time:
            body['end_time'] = end_time

        return self.send_request(action, body)

    def describe_volumes(self,
                         volumes = None,
                         instance_id = None,
                         status = None,
                         transition_status = None,
                         volume_name = None,
                         verbose = 0,
                         offset = None,
                         limit = None,
                         **params):
        """ Action:DescribeVolumes
            @param volumes : the array of IDs of volumes.
            @param instance_id: ID of the instance that volume is currently attached to, if has.
            @param status: pending, available, in-use, deleted.
            @param transition_status: Status of the volume in transition, including creating, deleting, attaching, detaching.
            @param verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
            @param volume_name: the name of the volume. Support partial match.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_VOLUMES
        body = {}
        if volumes:
            body['volumes'] = volumes
        if instance_id:
            body['instance_id'] = instance_id
        if status:
            body['status'] = status
        if transition_status:
            body['transition_status'] = transition_status
        if volume_name:
            body['volume_name'] = volume_name
        if verbose:
            body['verbose'] = verbose
        if offset:
            body['offset'] = offset
        if limit :
            body['limit'] = limit

        return self.send_request(action, body)

    def create_volumes(self, size,
                             volume_name = "",
                             count = 1,
                              **params):
        """ Action:CreateVolumes
            @param size : The size of each volume. Unit is GB.
            @param vol_replicas : the replica factor of volume
            @param volume_name : the short name of volume
            @param count : The number of volumes to create.
        """
        action = ACTION_CREATE_VOLUMES
        body = {'size' : size,
                'volume_name' : volume_name,
                'count' : count,
                }

        return self.send_request(action, body)

    def delete_volumes(self, volumes,
                              **params):
        """ Action:DeleteVolumes
            @param volumes : An array including IDs of the volumes you want to delete.
        """

        action = ACTION_DELETE_VOLUMES
        body = {}
        body["volumes"] = volumes

        return self.send_request(action, body)

    def attach_volumes(self, volumes,
                       instance,
                       **params):
        """ Action:AttachVolumes
            @param volumes : An array including IDs of the volumes you want to attach.
            @param instance : the ID of instance the volumes will be attached to.
        """

        action = ACTION_ATTACH_VOLUMES
        body = {"volumes" : volumes,
                "instance" : instance
               }

        return self.send_request(action, body)

    def detach_volumes(self, volumes,
                       instance,
                       **params):
        """ Action:DetachVolumes
            @param volumes : An array including IDs of the volumes you want to attach.
            @param instance : the ID of instance the volumes will be detached from.
        """

        action = ACTION_DETACH_VOLUMES
        body = {"volumes" : volumes,
                "instance" : instance
               }

        return self.send_request(action, body)

    def resize_volumes(self,
                       volumes,
                       size,
                       **params):
        """ Action:ResizeVolumes
            @param volumes: The IDs of the volumes you want to resize.
            @param size : The new size of the volumes. Unit is GB
        """
        # build params
        action = ACTION_RESIZE_VOLUMES
        body = {}
        body["size"] = int(size)
        body['volumes'] = volumes

        return self.send_request(action, body)

    def modify_volume_attributes(self, volume,
                                       volume_name = None,
                                       description = None,
                                       **params):
        """ @param volume:  the ID of volume whose attributes you want to modify.
            @param volume_name: Name of the volume. It's a short name for
                                the volume that more meaningful than volume id.
            @param description: The detailed description of the resource.
        """
        action = ACTION_MODIFY_VOLUME_ATTRIBUTES
        body = {}
        if volume:
            body["volume"] = volume
        if volume_name is not None:
            body['volume_name'] = volume_name
        if description is not None:
            body['description'] = description

        return self.send_request(action, body)

    def describe_key_pairs(self, keypairs = None,
                                 encrypt_method = None,
                                 keypair_name = None,
                                 verbose = 0,
                                 offset = None,
                                 limit = None,
                                 **params):
        """ Action: DESCRIBE_KEY_PAIRS
            @param keypairs: IDs of the keypairs you want to describe.
            @param encrypt_method: encrypt method.
            @param keypair_name: the name of the key pair. Support partial match.
            @param verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_KEY_PAIRS
        body = {}
        if keypairs:
            body['keypairs'] = keypairs
        if encrypt_method:
            body['encrypt_method'] = encrypt_method
        if keypair_name:
            body['keypair_name'] = keypair_name
        if verbose:
            body['verbose'] = verbose
        if offset:
            body['offset'] = offset
        if limit :
            body['limit'] = limit

        return self.send_request(action, body)

    def attach_keypairs(self, keypairs,
                            instances,
                              **params):
        """ @param keypairs: IDs of the keypairs you want to attach to instance .
            @param instances: IDs of the instances the keypairs will be attached to.
        """

        action = ACTION_ATTACH_KEY_PAIRS
        body = {}
        if keypairs:
            body['keypairs'] = keypairs
        if instances:
            body['instances'] = instances

        return self.send_request(action, body)

    def detach_keypairs(self, keypairs,
                            instances,
                              **params):
        """ @param keypairs: IDs of the keypairs you want to detach from instance .
            @param instances: IDs of the instances the keypairs will be detached from.
        """

        action = ACTION_DETACH_KEY_PAIRS
        body = {}
        if keypairs:
            body['keypairs'] = keypairs
        if instances:
            body['instances'] = instances

        return self.send_request(action, body)

    def create_keypair(self, keypair_name,
                       mode = 'system',
                       encrypt_method = "ssh-rsa",
                       public_key = None,
                       **params):
        """ @param keypair_name: The name of the keypair you want to create.
            @param encrypt_method: The encrypt method, supported methods "ssh-rsa", "ssh-dss".
        """

        action = ACTION_CREATE_KEY_PAIR
        body = {}
        if mode:
            body['mode'] = mode
        if keypair_name:
            body['keypair_name'] = keypair_name
        if encrypt_method:
            body['encrypt_method'] = encrypt_method
        if public_key:
            body['public_key'] = public_key

        return self.send_request(action, body)

    def delete_keypairs(self, keypairs,
                              **params):
        """ @param keypairs: IDs of the keypairs you want to delete.
        """

        action = ACTION_DELETE_KEY_PAIRS
        body = {}
        if keypairs:
            body['keypairs'] = keypairs

        return self.send_request(action, body)

    def modify_keypair_attributes(self, keypair,
                                  keypair_name = None,
                                  description = None,
                                  **params):
        """
            @param keypair: the ID of keypair you want to modify its attributes.
            @param keypair_name: the new name of keypair.
            @param description: The detailed description of the resource.
        """
        action = ACTION_MODIFY_KEYPAIR_ATTRIBUTES
        body = {}
        if keypair:
            body['keypair'] = keypair
        if keypair_name is not None:
            body['keypair_name'] = keypair_name
        if description is not None:
            body['description'] = description

        return self.send_request(action, body)

    def get_private_key(self,
                        keypair,
                        **params):
        """
            @param owner: the ID of of user.
            @param keypair: the ID of keypair.
        """
        action = ACTION_GET_PRIVATE_KEY
        body = {}
        if keypair:
            body['keypair'] = keypair

        return self.send_request(action, body)

    def describe_security_groups(self, security_groups = None,
                                 security_group_name = None,
                                 verbose = 0,
                                 offset = None,
                                 limit = None,
                                 **params):
        """ @param security_groups: IDs of the security groups you want to describe.
            @param security_group_name: the name of the security group.
            @param verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_SECURITY_GROUPS
        body = {}
        if security_groups:
            body['security_groups'] = security_groups
        if security_group_name:
            body['security_group_name'] = security_group_name
        if verbose:
            body['verbose'] = verbose
        if offset:
            body['offset'] = int(offset)
        if limit :
            body['limit'] = int(limit)

        return self.send_request(action, body)

    def create_security_group(self, security_group_name,
                              **params):
        """
            @param security_group_name: the name of the security group you want to create.
        """
        action = ACTION_CREATE_SECURITY_GROUP
        body = {}
        if security_group_name:
            body['security_group_name'] = security_group_name

        return self.send_request(action, body)

    def modify_security_group_attributes(self,
                                         security_group,
                                         security_group_name = None,
                                         description = None,
                                         rules = None,
                                         **params):
        """
            @param security_group: the ID of the security group whose content you
                                      want to update.
            @param security_group_name: the new group name you want to update.
            @param rules: a list of rules you want to overwrite the original ones.
            @param description: The detailed description of the resource.
        """
        action = ACTION_MODIFY_SECURITY_GROUP_ATTRIBUTES
        body = {}
        body['security_group'] = security_group
        if rules:
            body['rules'] = rules
        if security_group_name is not None:
            body['security_group_name'] = security_group_name
        if description is not None:
            body['description'] = description

        return self.send_request(action, body)

    def apply_security_group(self,
                              security_group,
                              instances = None,
                              **params):
        """
            @param security_group: the ID of the security group that you
                                      want to apply to instances.
            @param instances: the IDs of the instances you want to apply the security group.
        """
        action = ACTION_APPLY_SECURITY_GROUP
        body = {}
        if security_group:
            body['security_group'] = security_group
        if instances:
            body['instances'] = instances
        return self.send_request(action, body)

    def delete_security_groups(self, security_groups,
                               **params):
        """
            @param security_groups: the IDs of the security groups you want to delete.
        """
        action = ACTION_DELETE_SECURITY_GROUPS
        body = {}
        if security_groups:
            body['security_groups'] = security_groups

        return self.send_request(action, body)

    def describe_security_group_rules(self,
                                      security_group = None,
                                      security_group_rules = None,
                                      direction = None,
                                      offset = None,
                                      limit = None,
                                      **params):
        """ @param security_group: the ID of the security group whose rules you want to describe.
            @param security_group_rules: the IDs of the security group rules you want to describe.
            @param direction: 0 for inbound; 1 for outbound
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_SECURITY_GROUP_RULES
        body = {}
        if security_group:
            body['security_group'] = security_group
        if security_group_rules:
            body['security_group_rules'] = security_group_rules
        if direction is not None:
            body['direction'] = direction
        if offset:
            body['offset'] = int(offset)
        if limit :
            body['limit'] = int(limit)

        return self.send_request(action, body)

    def add_security_group_rules(self,
                                 security_group,
                                 rules,
                                 **params):
        """
            @param security_group: the ID of the security group whose rules you
                                      want to add.
            @param rules: a list of rules you want to add.
        """
        action = ACTION_ADD_SECURITY_GROUP_RULES
        body = {}
        body['security_group'] = security_group
        if rules:
            body['rules'] = rules

        return self.send_request(action, body)

    def delete_security_group_rules(self,
                                    security_group_rules,
                                    **params):
        """
            @param security_group_rules: the IDs of rules you want to delete.
        """
        action = ACTION_DELETE_SECURITY_GROUP_RULES
        body = {}
        body['security_group_rules'] = security_group_rules

        return self.send_request(action, body)

    def modify_security_group_rule_attributes(self,
                                              security_group_rule,
                                              priority,
                                              **params):
        """
            @param security_group_rule: the ID of the security group rule whose attributes you
                                      want to update.
            @param priority: priority [0 - 100].
        """
        action = ACTION_MODIFY_SECURITY_GROUP_RULE_ATTRIBUTES
        body = {}
        body['security_group_rule'] = security_group_rule
        body['priority'] = priority

        return self.send_request(action, body)

    def describe_vxnets(self, vxnets = None,
                        vxnet_name = None,
                        verbose = 0,
                        limit = None,
                        offset = None,
                        **params):
        """
            @param vxnets: the IDs of vxnets you want to describe.
            @param vxnet_name: the name of the vxnet.
            @param verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_VXNETS
        body = {}
        if vxnets:
            body['vxnets'] = vxnets
        if vxnet_name:
            body['vxnet_name'] = vxnet_name
        if verbose:
            body['verbose'] = verbose
        if offset:
            body['offset'] = int(offset)
        if limit :
            body['limit'] = int(limit)

        return self.send_request(action, body)

    def create_vxnets(self,
                      vxnet_name,
                      vxnet_type=1,
                      count=1,
                      **params):
        """
            @param vxnet_name: the name of vxnet you want to create.
            @param vxnet_type: vxnet type. 0: unmanaged vxnet, 1: managed vxnet.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_CREATE_VXNETS
        body = {}
        if vxnet_name:
            body['vxnet_name'] = vxnet_name
        if vxnet_type is not None:
            body['vxnet_type'] = vxnet_type
        if count:
            body['count'] = count

        return self.send_request(action, body)

    def join_vxnet(self,
                   vxnet,
                   instances, **params):
        """ Action:JoinVxnet
            @param vxnet : the id of vxnet you want the instances to join.
            @param instances : the IDs of instances that will join vxnet.
        """

        action = ACTION_JOIN_VXNET
        body = {}
        if vxnet:
            body['vxnet'] = vxnet
        if instances:
            body['instances'] = instances

        return self.send_request(action, body)

    def leave_vxnet(self,
                    vxnet,
                    instances, **params):
        """ Action:LeaveVxnet
            @param vxnet : The id of vxnet that the instances will leave.
            @param instances : the IDs of instances that will leave vxnet.
        """

        action = ACTION_LEAVE_VXNET
        body = {}
        if vxnet:
            body['vxnet'] = vxnet
        if instances:
            body['instances'] = instances

        return self.send_request(action, body)

    def delete_vxnets(self, vxnets,
                        **params):
        """
            @param vxnets: the IDs of vxnets you want to delete.
        """
        action = ACTION_DELETE_VXNETS
        body = {}
        if vxnets:
            body['vxnets'] = vxnets

        return self.send_request(action, body)

    def modify_vxnet_attributes(self, vxnet,
                                vxnet_name = None,
                                description = None,
                                **params):
        """
            @param vxnet: the ID of vxnet you want to modify its attributes.
            @param vxnet_name: the new name of vxnet.
            @param description: The detailed description of the resource.
        """
        action = ACTION_MODIFY_VXNET_ATTRIBUTES
        body = {}
        if vxnet:
            body['vxnet'] = vxnet
        if vxnet_name is not None:
            body['vxnet_name'] = vxnet_name
        if description is not None:
            body['description'] = description

        return self.send_request(action, body)

    def describe_vxnet_instances(self,
                                 vxnet,
                                 instances = None,
                                 image = None,
                                 instance_type = None,
                                 status = None,
                                 owner = None,
                                 verbose = 0,
                                 limit = None,
                                 offset = None,
                                 **params):
        """
            @param vxnet: the ID of vxnet whose instances you want to describe.
            @param image: filter by image ID.
            @param instances: filter by instance ID.
            @param instance_type: filter by instance type
            @param status: filter by status
            @param owner: filter by owner
            @param verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_VXNET_INSTANCES
        body = {}
        if vxnet:
            body['vxnet'] = vxnet
        if instances:
            body['instances'] = instances
        if image:
            body['image'] = image
        if instance_type:
            body['instance_type'] = instance_type
        if status:
            body['status'] = status
        if owner:
            body['owner'] = owner
        if verbose:
            body['verbose'] = verbose
        if offset:
            body['offset'] = int(offset)
        if limit :
            body['limit'] = int(limit)

        return self.send_request(action, body)



    def describe_routers(self,
                        routers = None,
                        vxnet = None,
                        status = None,
                        owner = None,
                        verbose = 0,
                        console = None,
                        limit = None,
                        offset = None,
                        **params):
        """
            @param routers: the IDs of the routers you want to describe.
            @param vxnet: the ID of vxnet you want to describe.
            @param owner: only describe vxnets belong to this owner.
            @param verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_ROUTERS
        body = {}
        if routers:
            body['routers'] = routers
        if vxnet:
            body['vxnet'] = vxnet
        if status:
            body['status'] = status
        if verbose:
            body['verbose'] = verbose
        if offset:
            body['offset'] = int(offset)
        if limit :
            body['limit'] = int(limit)

        return self.send_request(action, body)

    def create_routers(self,
                      count=1,
                      router_name=None,
                      security_group=None,
                      **params):
        """
            @param router_name: the name of the router.
            @param security_group: the ID of the security_group you want to apply to router.
            @param count: the count of router you want to create.
        """
        action = ACTION_CREATE_ROUTERS
        body = {}
        if router_name:
            body['router_name'] = router_name
        if security_group:
            body['security_group'] = security_group
        body["count"] = int(count)

        return self.send_request(action, body)

    def delete_routers(self,
                      routers,
                      **params):
        """
            @param routers: the IDs of routers you want to delete.
        """
        action = ACTION_DELETE_ROUTERS
        body = {}
        if routers:
            body['routers'] = routers

        return self.send_request(action, body)

    def update_routers(self,
                      routers,
                      **params):
        """
            @param routers: the IDs of routers you want to update.
        """
        action = ACTION_UPDATE_ROUTERS
        body = {}
        if routers:
            body['routers'] = routers

        return self.send_request(action, body)

    def poweroff_routers(self,
                         routers,
                         **params):
        """
            @param routers: the IDs of routers you want to poweroff.
        """
        action = ACTION_POWEROFF_ROUTERS
        body = {}
        if routers:
            body['routers'] = routers

        return self.send_request(action, body)

    def poweron_routers(self,
                        routers,
                        **params):
        """
            @param routers: the IDs of routers you want to poweron.
        """
        action = ACTION_POWERON_ROUTERS
        body = {}
        if routers:
            body['routers'] = routers

        return self.send_request(action, body)

    def resize_routers(self,
                       routers,
                       router_type,
                       **params):
        """
            @param routers: the IDs of routers you want to resize.
        """
        action = ACTION_RESIZE_ROUTERS
        body = {}
        body['router_type'] = router_type
        if routers:
            body['routers'] = routers

        return self.send_request(action, body)

    def join_router(self,
                    vxnet,
                    router,
                    ip_network,
                    features=1,
                    **params):
        """
            @param vxnet: the ID of vxnet that will join the router.
            @param router: the ID of the router the vxnet will join.
            @param features: the feature the vxnet will enable in the router.
                             1 - dhcp server.
            @param ip_network: the ip network in CSI format.
        """
        action = ACTION_JOIN_ROUTER
        body = {}
        if router:
            body['router'] = router
        if vxnet:
            body['vxnet'] = vxnet
        if features is not None:
            body['features'] = features
        if ip_network:
            body['ip_network'] = ip_network

        return self.send_request(action, body)

    def leave_router(self,
                     router,
                     vxnets,
                     **params):
        """
            @param vxnets: the IDs of vxnets that will leave the router.
            @param router: the ID of the router the vxnet will leave.
        """
        action = ACTION_LEAVE_ROUTER
        body = {}
        if router:
            body['router'] = router
        if vxnets:
            body['vxnets'] = vxnets

        return self.send_request(action, body)

    def modify_router_attributes(self,
                                 router,
                                 vxnet=None,
                                 features=None,
                                 eip=None,
                                 security_group=None,
                                 router_name=None,
                                 description=None,
                                 **params):
        """
            @param router: the ID of router you want to modify its attributes.
            @param vxnet: the ID of vxnet whose feature you want to modify.
            @param features: the feature for vxnet.
            @param eip: the eip.
            @param security_group: the ID of the security_group you want to apply to router.
            @param router_name: the name of the router.
            @param description: the description of the router.
        """
        action = ACTION_MODIFY_ROUTER_ATTRIBUTES
        body = {}
        if router:
            body['router'] = router
        if vxnet:
            body['vxnet'] = vxnet
        if features is not None:
            body['features'] = features
        if eip is not None:
            body['eip'] = eip
        if security_group:
            body['security_group'] = security_group
        if router_name is not None:
            body['router_name'] = router_name
        if description is not None:
            body['description'] = description

        return self.send_request(action, body)

    def describe_router_vxnets(self,
                                router=None,
                                vxnet=None,
                                limit=None,
                                offset=None,
                                **params):
        """
            @param router: filter by router ID.
            @param vxnet: filter by vxnet ID.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_ROUTER_VXNETS
        body = {}
        if router:
            body['router'] = router
        if vxnet:
            body['vxnet'] = vxnet
        if offset:
            body['offset'] = int(offset)
        if limit :
            body['limit'] = int(limit)

        return self.send_request(action, body)

    def describe_router_statics(self,
                                router_statics = None,
                                router = None,
                                vxnet = None,
                                static_type = None,
                                owner = None,
                                verbose = 0,
                                console = None,
                                limit = None,
                                offset = None,
                                **params):
        """
            @param router_statics: the IDs of the router statics you want to describe.
            @param router: filter by router ID.
            @param vxnet: filter by vxnet ID.
            @param static_type: 0: fixed ips, 1: port forwarding.
            @param owner: only describe vxnets belong to this owner.
            @param verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_ROUTER_STATICS
        body = {}
        if router_statics:
            body['router_statics'] = router_statics
        if router:
            body['router'] = router
        if vxnet:
            body['vxnet'] = vxnet
        if static_type is not None:
            body['static_type'] = static_type
        if verbose:
            body['verbose'] = verbose
        if offset:
            body['offset'] = int(offset)
        if limit :
            body['limit'] = int(limit)

        return self.send_request(action, body)

    def add_router_statics(self,
                           router,
                           statics,
                           **params):
        """
            @param router: the ID of the router whose statics you want to add.
            @param statics: a list of statics you want to add.
        """
        action = ACTION_ADD_ROUTER_STATICS
        body = {}
        if router:
            body['router'] = router
        if statics:
            body['statics'] = statics

        return self.send_request(action, body)

    def delete_router_statics(self,
                              router_statics,
                              **params):
        """
            @param router_statics: the IDs of router statics you want to delete.
        """
        action = ACTION_DELETE_ROUTER_STATICS
        body = {}
        body['router_statics'] = router_statics

        return self.send_request(action, body)

    def get_vpn_certs(self,
                      router,
                      **params):
        """
            @param router: the ID of router whose VPN certificates you want to get.
        """
        action = ACTION_GET_VPN_CERTS
        body = {}
        body['router'] = router

        return self.send_request(action, body)

    def describe_eips(self,
                      eips = None,
                      status = None,
                      eip_group = None,
                      eip_name = None,
                      search_word = None,
                      offset = None,
                      limit = None,
                      **params):
        """
            @param eips: IDs of the eip you want describe.
            @param status: filter eips by status
            @param eip_group: filter eips by eip group.
            @param eip_name: the name of the eip. Support partial match.
            @param search_word: search word column.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """

        action = ACTION_DESCRIBE_EIPS
        body = {}
        if eips:
            body['eips'] = eips
        if status:
            body['status'] = status
        if eip_group:
            body['eip_group'] = eip_group
        if eip_name:
            body['eip_name'] = eip_name
        if search_word:
            body['search_word'] = search_word
        if offset:
            body['offset'] = int(offset)
        if limit :
            body['limit'] = int(limit)

        return self.send_request(action, body)

    def associate_eip(self,
                      eip,
                      instance,
                      **params):
        """
            @param eip: The id of eip you want to associate with instance.
            @param instance: the id of instance you want to associate eip.
        """

        action = ACTION_ASSOCIATE_EIP
        body = {}
        if eip:
            body['eip'] = eip
        if instance:
            body['instance'] = instance

        return self.send_request(action, body)

    def dissociate_eips(self,
                        eips,
                        **params):
        """
            @param eips: The ids of eips you want to dissociate with instance.
        """

        action = ACTION_DISSOCIATE_EIPS
        body = {}
        if eips:
            body['eips'] = eips

        return self.send_request(action, body)

    def allocate_eips(self,
                      bandwidth,
                      count=1,
                      need_icp=0,
                      eip_group=None,
                      eip_name='',
                      **params):
        """
            @param count: the number of eips you want to allocate.
            @param bandwidth: the bandwidth of the eip in Mbps.
            @param eip_name : the short name of eip
            @param eip_group: the ID of eip group you want to allocate eip from.
        """
        action = ACTION_ALLOCATE_EIPS
        body = {}
        if count:
            body['count'] = count
        if bandwidth:
            body['bandwidth'] = bandwidth
        if eip_name:
            body['eip_name'] = eip_name
        if eip_group:
            body['eip_group'] = eip_group
        body['need_icp'] = need_icp

        return self.send_request(action, body)

    def release_eips(self,
                     eips,
                     force=0,
                     **params):
        """
            @param eips : The ids of eips that you want to release
            @param force : Whether to force release the eip that needs icp codes.
        """
        action = ACTION_RELEASE_EIPS
        body = {}
        if eips:
            body['eips'] = eips
        body['force'] = 0 if force == 0 else 1

        return self.send_request(action, body)

    def change_eips_bandwidth(self,
                              eips,
                              bandwidth,
                              **params):
        """
            @param eips: The IDs of the eips whose bandwidth you want to change.
            @param bandwidth: the new bandwidth of the eip in MB.
        """
        action = ACTION_CHANGE_EIPS_BANDWIDTH
        body = {}
        if bandwidth:
            body['bandwidth'] = bandwidth
        if eips:
            body['eips'] = eips

        return self.send_request(action, body)

    def modify_eip_attributes(self,
                              eip,
                              eip_name=None,
                              description=None,
                              need_icp=None,
                              icp_codes=None,
                              **params):
        """
            @param eip : The id of eip that you want to modify its attributes
        """
        action = ACTION_MODIFY_EIP_ATTRIBUTES
        body = {}
        if eip:
            body['eip'] = eip
        if eip_name:
            body['eip_name'] = eip_name
        if description:
            body['description'] = description
        if icp_codes:
            body['icp_codes'] = icp_codes
        if need_icp is not None:
            body['need_icp'] = need_icp

        return self.send_request(action, body)

    def describe_jobs(self,
                      jobs = None,
                      job_action = None,
                      resource_ids = None,
                      verbose = 0,
                      status = None,
                      offset = None,
                      limit = None,
                      **params):
        """ Action:ACTION_DESCRIBE_JOBS
            @param zone - which availability zone the request will be send to.
            @param jobs : An array including IDs of jobs, ["j-1234567"]
            @param job_action: The action of the job.
            @param resource_ids: The resources id user want to search.
            @param status : pending, working, done with failure, successful
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_JOBS
        body = {}
        if jobs:
            body['jobs'] = jobs
        if job_action:
            body['job_action'] = job_action
        if resource_ids:
            body['resource_ids'] = resource_ids
        if verbose:
            body['verbose'] = verbose
        if status:
            body['status'] = status
        if offset:
            body['offset'] = offset
        if limit :
            body['limit'] = limit

        return self.send_request(action, body)

    def describe_instance_types(self, instance_types = None,
                              **params):
        """ Action: DescribeInstanceTypes
            @param instance_types: IDs of the instance_types you want describe.
        """
        action = ACTION_DESCRIBE_INSTANCE_TYPES
        body = {}
        if instance_types:
            body['instance_types'] = instance_types

        return self.send_request(action, body)

    def describe_zones(self, zones = None,
                             status = None,
                              **params):
        """ Action: DescribeZones
            @param zones: IDs of the zones you want describe.
            @param status: only the zones with this status will be described.
        """
        action = ACTION_DESCRIBE_ZONES
        body = {}
        if zones:
            body['zones'] = zones
        if status:
            body['status'] = status

        return self.send_request(action, body)

    def get_resource_summary(self,
                             resource_types=None,
                             **params):
        """ Action:GetResourceSummary
            @param resource_types - the specified resource types, None means all.
        """
        action = ACTION_GET_RESOURCE_SUMMARY
        body = {}
        if resource_types:
            body['resource_types'] = resource_types

        return self.send_request(action, body)

    def describe_access_keys(self, access_keys = None,
                                   offset = None,
                                   limit = None,
                                   **params):
        """ Action: DESCRIBE_KEY_PAIRS
            @param access_keys: IDs of the access_keys you want to describe.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_ACCESS_KEYS
        body = {}
        if access_keys:
            body['access_keys'] = access_keys
        if offset:
            body['offset'] = offset
        if limit :
            body['limit'] = limit

        return self.send_request(action, body)

    def create_access_key(self, **params):
        """
        """
        action = ACTION_CREATE_ACCESS_KEY
        body = {}

        return self.send_request(action, body)

    def delete_access_keys(self, access_keys, **params):
        """
            @param access_key: the ID of access key you want to delete.
        """
        action = ACTION_DELETE_ACCESS_KEYS
        body = {}
        if access_keys:
            body['access_keys'] = access_keys

        return self.send_request(action, body)

    def modify_access_key_attributes(self, access_key,
                                     access_key_name = None,
                                     description = None,
                                     **params):
        """
            @param access_key: the ID of access_key you want to modify its attributes.
            @param access_key_name: the new name of access_key.
            @param description: The detailed description of the resource.
        """
        action = ACTION_MODIFY_ACCESS_KEY_ATTRIBUTES
        body = {}
        if access_key:
            body['access_key'] = access_key
        if access_key_name is not None:
            body['access_key_name'] = access_key_name
        if description is not None:
            body['description'] = description

        return self.send_request(action, body)

    def modify_user_attributes(self,
                               user_name = None,
                               gravatar_email = None,
                               lang = None,
                               phone = None,
                               address = None,
                               gender = None,
                               birthday = None,
                               **params):
        """
            @param user_name: the new user name of the user you want to update.
            @param gravatar_email: the email address for gravatar.
            @param lang: user's language preferences, "en" or "zh-cn".
            @param phone: user's phone number
            @param address: user's living address
            @param gender: user's gender
            @param birthday: user's birthday
        """
        action = ACTION_MODIFY_USER_ATTRIBUTES
        body = {}
        if user_name is not None:
            body['user_name'] = user_name
        if gravatar_email is not None:
            body['gravatar_email'] = gravatar_email
        if lang:
            body['lang'] = lang
        if phone:
            body['phone'] = phone
        if address:
            body['address'] = address
        if gender:
            body['gender'] = gender
        if birthday:
            body['birthday'] = birthday

        return self.send_request(action, body)

    def change_password(self,
                       oldpasswd,
                       newpasswd,
                       **params):
        """
            @param oldpasswd: old password.
            @param newpasswd: new password.
        """
        action = ACTION_CHANGE_PASSWORD
        body = {}
        if oldpasswd:
            body['oldpasswd'] = oldpasswd
        if newpasswd:
            body['newpasswd'] = newpasswd

        return self.send_request(action, body)

    def change_email(self,
                     email,
                     **params):
        """
            @param email: the new email address.
        """
        action = ACTION_CHANGE_EMAIL
        body = {}
        if email:
            body['email'] = email

        return self.send_request(action, body)

    def send_email_veri_code(self, **params):
        """
            send email veri code
        """
        action = ACTION_SEND_EMAIL_VERI_CODE
        body = {}

        return self.send_request(action, body)

    def send_confirm_email(self, **params):
        """
            @param user: the ID of user you want to send confirm email to.
        """
        action = ACTION_SEND_CONFIRM_EMAIL
        body = {}

        return self.send_request(action, body)

    def get_balance(self, **params):
        """
        """
        action = ACTION_GET_BALANCE
        body = {}

        return self.send_request(action, body)

    def lease(self,
                resources,
                **params):
        """
            @param resources: a list of resource ids you want to lease
        """
        action = ACTION_LEASE
        body = {}
        if resources:
            body['resources'] = resources

        return self.send_request(action, body)

    def get_lease_info(self,
                       resource,
                       **params):
        """
            @param resource: the resource id you want to get its lease info
        """
        action = ACTION_GET_LEASE_INFO
        body = {}
        if resource:
            body['resource'] = resource

        return self.send_request(action, body)

    def get_price(self,
                  resources,
                  **params):
        """ Action: get price
        """
        action = ACTION_GET_PRICE
        body = {}
        if resources:
            body['resources'] = resources

        return self.send_request(action, body)

    def get_charge_records(self,
                           zone=None,
                           resource_type=None,
                           resource=None,
                           start_time=None,
                           end_time=None,
                           offset=None,
                           limit=None,
                           **params):
        """
            @param zone: filter charge records by zone.
            @param resource_type: filter charge records by resource type.
            @param resource: filter charge records by resource id
            @param start_time: filter records by specified starting timestamp.
            @param end_time: filter records by specified ending timestamp.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_GET_CHARGE_RECORDS
        body = {}
        if zone:
            body['zone'] = zone
        if resource_type:
            body['resource_type'] = resource_type
        if resource:
            body['resource'] = resource
        if start_time:
            body['start_time'] = start_time
        if end_time:
            body['end_time'] = end_time
        if offset:
            body['offset'] = offset
        if limit:
            body['limit'] = limit

        return self.send_request(action, body)

    def get_charge_resources(self,
                             zone=None,
                             resource_type=None,
                             start_time=None,
                             end_time=None,
                             offset=None,
                             limit=None,
                             **params):
        """
            @param zone: filter charge records by specified zone id.
            @param resource_type: filter charge records by resource type.
            @param start_time: filter records by specified starting timestamp.
            @param end_time: filter records by specified ending timestamp.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_GET_CHARGE_RESOURCES
        body = {}
        if zone:
            body['zone'] = zone
        if resource_type:
            body['resource_type'] = resource_type
        if start_time:
            body['start_time'] = start_time
        if end_time:
            body['end_time'] = end_time
        if offset:
            body['offset'] = offset
        if limit:
            body['limit'] = limit

        return self.send_request(action, body)

    def get_charge_summary(self,
                           zone=None,
                           start_time=None,
                           end_time=None,
                           offset=None,
                           limit=None,
                           **params):
        """
            @param zone: filter charge records by specified zone id.
            @param start_time: filter records by specified starting timestamp.
            @param end_time: filter records by specified ending timestamp.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_GET_CHARGE_SUMMARY
        body = {}
        if zone:
            body['zone'] = zone
        if start_time:
            body['start_time'] = start_time
        if end_time:
            body['end_time'] = end_time
        if offset:
            body['offset'] = offset
        if limit:
            body['limit'] = limit

        return self.send_request(action, body)

    def get_recharge_records(self,
                             charge_type=None,
                             start_time=None,
                             end_time=None,
                             offset=None,
                             limit=None,
                             **params):
        """
            @param charge_type: filter by charge_type, "recharge" or "discharge"
            @param start_time: filter records by specified starting timestamp.
            @param end_time: filter records by specified ending timestamp.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_GET_RECHARGE_RECORDS
        body = {}
        if charge_type:
            body['charge_type'] = charge_type
        if start_time:
            body['start_time'] = start_time
        if end_time:
            body['end_time'] = end_time
        if offset:
            body['offset'] = offset
        if limit:
            body['limit'] = limit

        return self.send_request(action, body)

    def describe_tickets(self, zone = None,
                         tickets = None,
                         status = None,
                         resource_type = None,
                         resource_id = None,
                         summary = None,
                         description = None,
                         search_word = None,
                         offset = None,
                         limit = None,
                         **params):
        """ Action:DescribeTickets
            @param zone - filter the tickets by zone id.
            @param tickets: An array including IDs of the tickets you want to list.
                            No ID specified means list all.
            @param status: Status of the ticket. Valid values include open, in-progress, closed.
            @param resource_type: the type of the regarding resource.
            @param resource_id: the regarding resource id
            @param summary: search by summary.
            @param description: search by description.
            @param search_word: search word column.
            @param offset: the starting offset of the returning results.
            @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_TICKETS
        body = {}
        if zone:
            body['zone'] = zone
        if tickets:
            body['tickets'] = tickets
        if status:
            body['status'] = status
        if resource_type:
            body['resource_type'] = resource_type
        if resource_id:
            body['resource_id'] = resource_id
        if summary:
            body['summary'] = summary
        if description:
            body['description'] = description
        if search_word:
            body['search_word'] = search_word
        if offset:
            body['offset'] = int(offset)
        if limit :
            body['limit'] = int(limit)

        return self.send_request(action, body)

    def open_ticket(self,summary,
                         description,
                         resource_type=None,
                         resource_id=None,
                         **params):
        """ Action:OpenTicket
            @param resource_type: the type of the regarding resource.
            @param resource_id: the regarding resource id
            @param summary: title like summary.
            @param description: detailed description.
        """
        action = ACTION_OPEN_TICKET
        body = {}
        if resource_type:
            body['resource_type'] = resource_type
        if resource_id:
            body['resource_id'] = resource_id
        if summary:
            body['summary'] = summary
        if description:
            body['description'] = description

        return self.send_request(action, body)

    def close_tickets(self, tickets,
                         **params):
        """ Action:CloseTickets
            @param tickets - the tickets to close.
        """
        action = ACTION_CLOSE_TICKETS
        body = {}
        if tickets:
            body['tickets'] = tickets

        return self.send_request(action, body)

    def add_ticket_reply(self, ticket,
                         content,
                         **params):
        """ Action:AddTicketReply
            @param ticket - the ticket you want to add reply to.
            @param content - the reply content
        """
        action = ACTION_ADD_TICKET_REPLY
        body = {}
        if ticket:
            body['ticket'] = ticket
        if content:
            body['content'] = content

        return self.send_request(action, body)

    def describe_ticket_replies(self,
                                ticket = None,
                                offset = None,
                                limit = None,
                                **params):
        """
        @param ticket: The ticket id whose replies you want to describe.
        @param offset: the starting offset of the returning results.
        @param limit: specify the number of the returning results.
        """
        action = ACTION_DESCRIBE_TICKET_REPLIES
        body = {}
        if ticket:
            body['ticket'] = ticket
        if offset:
            body['offset'] = int(offset)
        if limit :
            body['limit'] = int(limit)

        return self.send_request(action, body)